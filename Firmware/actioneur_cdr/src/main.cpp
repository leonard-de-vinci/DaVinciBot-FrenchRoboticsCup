#include <Arduino.h>
#include <Servo.h>
#include "ros.h"
#include <std_msgs/Bool.h>

Servo servo_Actionneur_1;
Servo servo_Actionneur_2;

int pin_Servo_1 = 3;
int pin_servo_2 = 11;

int angle_range = 0;
int angle_deploye = 90;

bool cote = false;
bool actif = false;

bool led=false;

ros::NodeHandle nh;

void callbackcote(const std_msgs::Bool& toggle_msg){
  cote = toggle_msg.data;
  led=!led;
  digitalWrite(13,led);
}
void callbackactif(const std_msgs::Bool& toggle_msg){
  actif = toggle_msg.data;
  led=!led;
  digitalWrite(13,led);
}
ros::Subscriber<std_msgs::Bool> subcote("/cote/", &callbackcote );
ros::Subscriber<std_msgs::Bool> subactif("/actif/", &callbackactif );

void setup() {
  // put your setup code here, to run once:
  servo_Actionneur_1.attach(pin_Servo_1);
  servo_Actionneur_1.write(angle_range);
  servo_Actionneur_2.attach(pin_servo_2);
  servo_Actionneur_2.write(angle_range);
  pinMode(13,OUTPUT);
  //ros
  nh.initNode();
  nh.subscribe(subcote);
  nh.subscribe(subactif);
}

void loop() 
{
  nh.spinOnce();
  if(cote)
  {
    servo_Actionneur_2.write(angle_range);
    if(actif){
      servo_Actionneur_1.write(angle_deploye);
    }
    else {
    servo_Actionneur_1.write(angle_range);
    } 
  }
  else{
    servo_Actionneur_1.write(angle_range);
    if(actif){
      servo_Actionneur_2.write(angle_deploye);
    }else {
      servo_Actionneur_2.write(angle_range);
    }
  }
  delay(100);
}