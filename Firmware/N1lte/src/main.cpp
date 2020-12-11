#include "TimerOne.h"
#include <Arduino.h>
#include "header.h"

void setup(void)
{
  //ROS
  nh.initNode();
  //initialisation du Node ROS
  nh.advertise(pub_reality);         //advertise le topic de publication
  nh.subscribe(sub_target);
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence
  //TIMER initialization
  Timer1.initialize(period);     //initialisation du timer
  Timer1.attachInterrupt(Cycle); //attachInterrupt
  //pin init
  pinMode(pin_pwr, OUTPUT);
  digitalWrite(pin_pwr,LOW);
  pinMode(pin_dir1, OUTPUT);
  digitalWrite(pin_dir1,LOW);
  pinMode(pin_dir2, OUTPUT);
  digitalWrite(pin_dir2,LOW);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(pin_encoder, INPUT);
  while (!nh.connected())
  {
    nh.spinOnce();
    digitalWrite(LED_BUILTIN, HIGH);
    delay(100);
    digitalWrite(LED_BUILTIN, LOW);
    delay(100);
  }
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
      if(!nh.connected()){
        emergency_break = true;
      }
      n=0;
    }
    // ros pub
    reality_pub.ticks = reality_ticks; //reality_ticks;
    reality_pub.dir = dir;
    pub_reality.publish(&reality_pub);
    nh.spinOnce();
    mainlooppub = false;
  }
  digitalWrite(LED_BUILTIN, emergency_break);
}

void Cycle() ///called by the timer
{
  cli(); //éteint les interrupts
  copytick = tick; //
  tick=0;
  sei(); //relance les interrupts
  if (emergency_break)
  {
    motorbreak();
  } else 
  {
    //calculate error and pid
    e = target_ticks - copytick;
    E = E + e;
    E = ( E < 0) ? 0 : E;
    E = ( E < IMAX) ? E : IMAX;
    PID_ = (kp * e) + (ki*E); 
    mapped = ( PID_ < 0) ? 0 : PID_;
    mapped = ( PID_ < 1023) ? PID_ : 1023;
    analogWrite(pin_pwr, mapped);
    
  }
  reality_ticks = copytick;
  mainlooppub = true;
}

void encoderInterrupt()
{
  tick++;
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
  else
  {
    digitalWrite(pin_pwr,LOW);
    digitalWrite(pin_dir1, dir);
    digitalWrite(pin_dir2, !dir);
  }
}
void target_callback(const PID::speed &msg)
{
  target_ticks = msg.ticks;
  if(dir != msg.dir && (!emergency_break)){
    digitalWrite(pin_pwr,LOW);
    digitalWrite(pin_dir1, dir);
    digitalWrite(pin_dir2, !dir);
    dir = msg.dir;
  }
  E = 0;
}