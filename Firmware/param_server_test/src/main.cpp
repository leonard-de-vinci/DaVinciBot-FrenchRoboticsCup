#include <Arduino.h>
#include <ros.h>


//create your handle
ros::NodeHandle nh;

char buffer[250];
int pid_constants[3];

void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
    while (!nh.connected()) {
        nh.spinOnce();
    }
    nh.loginfo("initialised");
}

void loop(){
    if (! nh.getParam("rpid", pid_constants,3)) { 
        nh.loginfo("error");
        //default values
        pid_constants[0]= 0;
        pid_constants[1]=0;
        pid_constants[2]=0; 
    }
    char cstr[16];
    itoa(pid_constants[0], cstr, 10);
    nh.loginfo(cstr);
    digitalWrite(LED_BUILTIN, pid_constants[0]);
    nh.spinOnce();
    delay(100);
}