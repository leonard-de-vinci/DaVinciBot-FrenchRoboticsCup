#include "TimerOne.h"
#include <Arduino.h>
#include "header.h"

void setup(void)
{
  //ROS
  nh.initNode(); //initialisation du Node ROS
  nh.advertise(pub_reality); //advertise le topic de publication
  nh.subscribe(sub_target); //on s'abonne à là où on va écouter
  nh.subscribe(sub_emergency_break); //abonnement arrêt d'urgence

  //TIMER initialization
  Timer1.initialize(period); //initialisation du timer
  Timer1.attachInterrupt(Cycle); //attachInterrupt
  //encoder initialisation
  attachInterrupt(encoderpin,encoderInterrupt,RISING);
  //setting up pwm precision
  analogWriteFrequency(pwmpin1,F_CPU/1E6);//setting up ideal frequency pedending on cpu frequency
  analogWriteFrequency(pwmpin2,F_CPU/1E6);//setting up ideal frequency pedending on cpu frequency
  analogWriteResolution(10); // 0 - 255
  //ros here pls
}

void loop(void)
{
  if(target_cycles != old_cycles){
    // create new message
    //publish new message
    reality_pub.ticks = reality_ticks;
    reality_pub.cycles = target_cycles;
    pub_reality.publish(&reality_pub);
    old_cycles = target_cycles;
    
  }
}

void Cycle()
{
  cli(); //éteint les interrupts
  if(emergency_break){
    motorbreak();
  }else if(target_cycles>0){
    //calculate error and pid

    e = target_ticks - tick;
    E = E+e;
    de = e-olde;
    PID = (kp*e)+(ki*E)+(kd*de);
    mapped = map(PID,minpid,maxpid,0,1023);
    analogWrite(bucketpin,mapped);
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
  //! A FAIRE PLUS TARD
  digitalWrite(pwmpin1, HIGH);
  digitalWrite(pwmpin2, HIGH);
}
void emergency_break_callback(const std_msgs::Bool &msg)
{
  emergency_break = msg.data;
}
void target_callback(const PID::IntArr_ &msg)
{
  target_ticks = msg.data.ticks;
  target_cycles = msg.data.cycles;
  if(target_ticks > 0){
    bucketpin = pwmpin1;
    digitalWrite(pwmpin2, LOW);
  }
  else{
    bucketpin = pwmpin2;
    digitalWrite(pwmpin1, LOW);
    target_ticks *= -1;
  }
}