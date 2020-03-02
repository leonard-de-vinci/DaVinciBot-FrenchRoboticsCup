#include <NewPing.h>
#include <ros.h>
#include <Arduino.h>
#include <std_msgs/Float32MultiArray.h>

//define the constants
#define SONAR_NUM 2
#define maxDistance 400
#define intervalR 60

ros::NodeHandle nh;
std_msgs::Float32MultiArray TopicMessage;
ros::Publisher pub_msgs_ultrasound("/ultrasounds", &TopicMessage);
unsigned long currentMicros;
NewPing ultrasonics[SONAR_NUM] = 
{
  NewPing(3, 2, maxDistance),
  NewPing(6, 7, maxDistance)
};

unsigned long range_timer;

void setup() {
  nh.initNode();
    
  while (!nh.connected()) {
      nh.spinOnce();
  }

  nh.loginfo("Finished setup");
}

void loop() {
  nh.loginfo("In the loop");
  currentMicros = micros();
 
  //if (currentMicros-range_timer >= intervalR)
  //{
    //range_timer = currentMicros + intervalR;
    
    TopicMessage.data[0] = ultrasonics[0].ping_cm();
    TopicMessage.data[1] = ultrasonics[1].ping_cm();

    pub_msgs_ultrasound.publish(&TopicMessage);
  //}

  nh.spinOnce();
}

