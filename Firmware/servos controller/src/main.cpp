#include <Arduino.h>
#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int8.h>

void servocallback(const std_msgs::Int8 &msg);

ros::NodeHandle nh;
ros::Subscriber<std_msgs::Int8> sub_servo("/servos", &servocallback);

Servo drapeau;
Servo brasDroit;
Servo piedGauche;
Servo piedDroit;
Servo brasGauche;
bool ledop = false;
bool mod[5] =   {false,false,false,false,false}; // false = rentré

// pin 9 -> drapeau (entre 35° et 130°)
// pin 6 -> bras droit (entre 10° et 80°)
// pin 11 -> pied droit (entre 10° et 90°)
// pin 5 -> pied gauche (entre 90° et 5°)
// pin 10 -> bras gauche (entre 16° et 100°)

void connect(){
  if(!nh.connected()){
    while (!nh.connected())
    {
      nh.spinOnce();
      digitalWrite(LED_BUILTIN,ledop);
      ledop = !ledop;
      delay(100);
    }

  }
}

void setup() {
  piedDroit.attach(11);
  piedGauche.attach(5);
  drapeau.attach(9);
  brasDroit.attach(6);
  brasGauche.attach(10);
  pinMode(LED_BUILTIN, OUTPUT);
  piedDroit.write(10);
  piedGauche.write(90);
  brasDroit.write(80);
  brasGauche.write(16);
  drapeau.write(35);
  nh.initNode();
  nh.subscribe(sub_servo);
  connect();
}

void loop() {
  nh.spinOnce();
}


void servocallback(const std_msgs::Int8 &msg){
  int i = msg.data;
  mod[i] = !mod[i];
  bool state = mod[i];
  switch (i)
  {
  case 0:
    piedGauche.write(state?5:90);
    break;
  case 1:
    brasDroit.write(state?10:80);
    break;
  case 2:
    drapeau.write(state?130:35);
    break;
  case 3:
    brasGauche.write(state?100:16);
    break;
  case 4:
    piedDroit.write(state?90:10);
  default:
    break;
  }
}