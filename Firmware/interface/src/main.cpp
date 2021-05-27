#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Int8.h>
#define led1 3
#define led2 4
#define led3 5
#define led4 6
#define led5 7
#define led6 8

#define switch1 A0
#define switch2 A1

#define tirrette A3

bool switcha = false;
bool switchb = false;
bool tire = false;
bool ledop = false;

std_msgs::Int8 msgs_pub;
ros::NodeHandle nh;
ros::Publisher pub_msgs("/start", &msgs_pub);

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
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  pinMode(led5,OUTPUT);
  pinMode(led6,OUTPUT);
  pinMode(LED_BUILTIN,OUTPUT);
  pinMode(switch1,INPUT);
  pinMode(switch2,INPUT);
  pinMode(tirrette,INPUT);
  nh.initNode();
  nh.advertise(pub_msgs);
  connect();
  nh.spinOnce();
}

void loop() {
  switcha = digitalRead(switch1);
  switchb = digitalRead(switch2);
  tire = digitalRead(tirrette);
  digitalWrite(led1,switcha);
  digitalWrite(led2,!switcha);
  digitalWrite(led3,switchb);
  digitalWrite(led4,!switchb);
  digitalWrite(led5,tire);
  digitalWrite(led6,!tire);
  digitalWrite(LED_BUILTIN,LOW);
  //ros
  //nh.loginfo((!tire && !switcha)? "yes":"no");
  if(tire && switcha){
    if(switchb){
      msgs_pub.data = 4;
    }else {
      msgs_pub.data = 16;
    }
  }else{
    msgs_pub.data = 0;
  }
  pub_msgs.publish(&msgs_pub);
  nh.spinOnce();
  connect();
  delay(10);

}