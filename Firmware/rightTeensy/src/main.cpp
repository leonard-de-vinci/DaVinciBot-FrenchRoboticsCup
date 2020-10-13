#include "TimerOne.h"
#include <Arduino.h>
#include "header.h"

void setup(void)
{
  pinMode(5, OUTPUT);
  digitalWriteFast(5, HIGH);
  //ROS
  nh.initNode(); //initialisation du Node ROS
  nh.advertise(pub_reality); //advertise le topic de publication
  nh.subscribe(sub_target); //on s'abonne à là où on va écouter
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence

  //TIMER initialization
  Timer1.initialize(period); //initialisation du timer
  Timer1.attachInterrupt(Cycle); //attachInterrupt
  //pin init
  pinMode(pin_pwr,OUTPUT);
  pinMode(pin_dir1,OUTPUT);
  pinMode(pin_dir2,OUTPUT);
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(pin_encoder,INPUT);
  //encoder initialisation
  attachInterrupt(digitalPinToInterrupt(pin_encoder),encoderInterrupt,RISING); //! slow must be changed to attachInterruptVector
  //attachInterruptVector(,encoderInterrupt,RISING);
  /*uint32_t mask = (0x09 << 16) | 0x01000000;//setup mask for rising edge
  volatile uint32_t *config;
  config = portConfigRegister(pin_encoder);
  */
  //setting up pwm precision
  analogWriteFrequency(pin_pwr,F_CPU/1E6);//setting up ideal frequency pedending on cpu frequency
  analogWriteResolution(10); // 0 - 255
}

void loop(void) ///main loop
{
  nh.spinOnce();
  if(target_cycles != old_cycles){
    // create new message
    reality_pub.ticks = reality_ticks;
    reality_pub.cycles = target_cycles;
    //publish new message
    pub_reality.publish(&reality_pub);
    old_cycles = target_cycles;
  }
  digitalWriteFast(LED_BUILTIN,emergency_break);
}

void Cycle()///called by the timer
{
  cli(); //éteint les interrupts
  if(emergency_break){
    motorbreak();
  }else if(target_cycles>0){
    //calculate error and pid
    e = target_ticks - tick;
    E = E+e;
    de = e-olde;
    PID_ = (kp*e)+(ki*E)+(kd*de);
    mapped = map(PID_,minpid,maxpid,0,1023);
    analogWrite(pin_pwr,mapped);
    //reset
    olde = e;
    reality_ticks = tick;
    tick = 0;
    target_cycles--;
  }
  sei(); //relance les interrupts
}

void encoderInterrupt(){
  tick++;
}

void motorbreak(){
  //! must be tested
  digitalWriteFast(pin_dir1, LOW);
  digitalWriteFast(pin_dir2, LOW);
}
void emergency_break_callback(const std_msgs::Bool &msg)
{
  emergency_break = msg.data;
  if(emergency_break){
    motorbreak();
  }else{
    digitalWriteFast(pin_dir1,dir);
    digitalWriteFast(pin_dir2,!dir);
  }
}
void target_callback(const PID::IntArr &msg)
{
  target_ticks = msg.ticks;
  target_cycles = msg.cycles;
  dir = target_ticks>0;
  target_ticks = abs(target_ticks);
  digitalWriteFast(pin_dir1,dir);
  digitalWriteFast(pin_dir2,!dir);
}