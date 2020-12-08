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
  //nh.subscribe(sub_empty);          //on s'abonne à là où on va écouter
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence
  while (!nh.connected())
  {
    nh.spinOnce();
  }
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
  //encoder initialisation
  attachInterrupt(digitalPinToInterrupt(pin_encoder), encoderInterrupt, RISING); //! slow must be changed to attachInterruptVector
  //attachInterruptVector(,encoderInterrupt,RISING);
  /*uint32_t mask = (0x09 << 16) | 0x01000000;//setup mask for rising edge
  volatile uint32_t *config;
  config = portConfigRegister(pin_encoder);
  */
  //setting up pwm precision
  analogWriteFrequency(pin_pwr, 10000); //setting up ideal frequency pedending on cpu frequency
  analogWriteResolution(10);                  // 0 - 255
}

void loop(void) ///main loop
{
  nh.spinOnce();
  if (mainlooppub)
  {
    // create new message

    reality_pub.ticks = reality_ticks; //reality_ticks;
    reality_pub.dir = dir;
    //publish new message
    pub_reality.publish(&reality_pub);
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
    //de = e - olde;
    PID_ = (kp * e); 
    int temp = (ki * E);// + (kd * de);
    int I = (temp < IMAX) ? temp : IMAX;
    PID_ +=I;
    mapped = ( PID_ < 0) ? 0 : PID_;
    mapped = ( PID_ < 1023) ? PID_ : 1023;
    analogWrite(pin_pwr, mapped);
    //reset
    //olde = e;
    
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
  //! must be tested
  digitalWrite(pin_pwr, LOW);
  digitalWrite(pin_dir1, HIGH);
  digitalWrite(pin_dir2, HIGH);
  //digitalWrite(pin_pwr,LOW);
  
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
  if(dir != msg.dir && !emergency_break){
    digitalWriteFast(pin_pwr,LOW);
    dir = msg.dir;
    digitalWrite(pin_dir1, dir);
    digitalWrite(pin_dir2, !dir);
  }
  E = 0;
  target_ticks = abs(target_ticks);
}