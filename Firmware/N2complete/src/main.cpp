#include "TimerOne.h"
#include <Arduino.h>
#include "header.h"

void setup(void)
{
  //ROS
  nh.initNode();
  nh.advertise(pub_reality);         //advertise le topic de publication
  nh.subscribe(sub_target);
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence
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
  while (!nh.connected())
  {
    nh.spinOnce();
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
    
  }
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
    reality_pub.ticks = reality_ticks; //reality_ticks;
    reality_pub.cycles = target_cycles;
    pub_reality.publish(&reality_pub);
    mainlooppub = false;
  }
  digitalWrite(LED_BUILTIN, emergency_break);
}

void Cycle() ///called by the timer
{
  cli(); //éteint les interrupts
  copytick = tick; //
  tick = 0;
  sei();
  if (emergency_break || (target_cycles<=0))
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
      PID_ =abs(PID_);
      digitalWrite(pin_dir1, dir);
      digitalWrite(pin_dir2, !dir);
    }
    mapped = ( PID_ < 1023) ? PID_ : 1023;
    analogWrite(pin_pwr, mapped);
    target_cycles--;
  }
  reality_ticks = copytick;
  mainlooppub = true;
}

void encoderInterrupt()
{
  if(digitalReadFast(pin_encoder2)){
    tick++;
  }else{
    tick--;
  }
}
void motorbreak()
{
  digitalWrite(pin_pwr, LOW);
  digitalWrite(pin_dir1, HIGH);
  digitalWrite(pin_dir2, HIGH);
  
}
void emergency_break_callback(const std_msgs::Bool &msg)
{
  emergency_break = msg.data;
  if (emergency_break)
  {
    motorbreak();
  }
}
void target_callback(const PID::IntArr &msg)
{
  target_ticks = msg.ticks;
  target_cycles = msg.cycles;
  E = 0;
}