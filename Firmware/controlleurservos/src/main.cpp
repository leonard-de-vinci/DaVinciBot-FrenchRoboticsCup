#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Int8.h>

void servocallback(const std_msgs::Int8 &msg);

ros::NodeHandle nh;
ros::Subscriber<std_msgs::Int8> sub_servo("/servos", &servocallback);


int servos[5] =     {  5,  6,  9, 10, 11};
int starts[5] =     {128,180,128,180,  0};
int ends[5] =       {140, 80,250, 80,255};
int expected[5] =   {128,128,128,180,128};
int mod[5] =   {0,0,0,0,0};
bool ledop = false;

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
  for( int i=0;i<5;i++){
    pinMode(servos[i],OUTPUT);
  }
  pinMode(LED_BUILTIN, OUTPUT);
  nh.initNode();
  nh.subscribe(sub_servo);
  connect();
}

void loop() {
  nh.spinOnce();
  for( int i=0;i<5;i++){
    analogWrite(servos[i],expected[i]);
  }
  ledop=!ledop;
  digitalWrite(LED_BUILTIN,ledop);
}

void servocallback(const std_msgs::Int8 &msg){
  int i = msg.data;
  mod[i] = (mod[i]+1)%2;
  if(mod[i]==0){
    expected[i]= starts[i];
  }else{
    expected[i] = ends[i];
  }

}