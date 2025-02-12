#include "TimerOne.h"
#include <Arduino.h>
#include "header.h"

void setup(void)
{
  
  //pin init
  pinMode(pin_pwr, OUTPUT);
  digitalWrite(pin_pwr,LOW);
  pinMode(pin_dir1, OUTPUT);
  digitalWrite(pin_dir1,LOW);
  pinMode(pin_dir2, OUTPUT);
  digitalWrite(pin_dir2,LOW);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pin_encoder, INPUT);
  pinMode(pin_encoder2,INPUT);
  //ROS
  nh.initNode();
  nh.advertise(pub_reality);         //advertise le topic de publication
  nh.subscribe(sub_target);
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence
  connect();
    //TIMER initialization
  Timer1.initialize(period);     //initialisation du timer
  Timer1.attachInterrupt(Cycle); //attachInterrupt
  //encoder initialisation
  attachInterrupt(digitalPinToInterrupt(pin_encoder), encoderInterrupt, RISING); //! slow must be changed to attachInterruptVector
  analogWriteFrequency(pin_pwr, 10000); //setting up ideal frequency pedending on cpu frequency
  analogWriteResolution(10);                  // 0 - 1023
}

void loop(void) ///main loop
{
  nh.spinOnce();
  if (mainlooppub)
  {
    n++;
    if(n >= TIMEOUT){
      connect();
      n=0;
    }
    reality_pub.data = copytick; //reality_ticks;
    pub_reality.publish(&reality_pub);
    mainlooppub = false;
  }
  digitalWriteFast(LED_BUILTIN, emergency_break);
}

void Cycle() ///called by the timer
{
  cli(); //éteint les interrupts
  copytick = tick; //
  tick = 0;
  sei();
  if (emergency_break)
  {
    motorbreak();
  } else 
  {
    //calculate error and pid
    e = target_ticks - copytick;
    E = E + e;
    E = ( E < IMIN) ? IMIN : E;
    E = ( E < IMAX) ? E : IMAX;
    PID_ = (kp * e)+(ki * E);
    if(dir!=(PID_>0)){
      dir = (PID_>0);
      digitalWrite(pin_dir1, !dir);
      digitalWrite(pin_dir2, dir);
    }
    PID_ =abs(PID_);
    mapped = ( PID_ < 1023) ? PID_ : 1023;
    analogWrite(pin_pwr, mapped);
  }
  mainlooppub = true;
}

void encoderInterrupt()
{
  if(digitalReadFast(pin_encoder2)){
    tick--;
  }else{
    tick++;
  }
}
void motorbreak()
{
  digitalWrite(pin_pwr, LOW);
  digitalWrite(pin_dir1, HIGH);
  digitalWrite(pin_dir2, HIGH);
  E=0;
}
void emergency_break_callback(const std_msgs::Bool &msg)
{
  emergency_break = msg.data;
  if (emergency_break)
  {
    motorbreak();
  }
}
void target_callback(const std_msgs::Int8 &msg)
{
  target_ticks = msg.data;
}
void connect(){
  if(!nh.connected()){
    while (!nh.connected())
    {
      motorbreak();
      nh.spinOnce();
      digitalWrite(LED_BUILTIN, HIGH);
      delay(80);
      digitalWrite(LED_BUILTIN, LOW);
      delay(80);
    }

  }
}