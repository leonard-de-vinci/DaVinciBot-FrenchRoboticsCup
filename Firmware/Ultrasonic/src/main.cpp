#include "NewPing.h"
#include <ros.h>
#include <sensor_msgs/Range.h>
#include <list>

//define the constants
#define maxDistance 400
#define intervalR 200

ros::NodeHandle nh;
ros::Publisher pub_range_ultrasound("/ultrasound", &range_msg);
std::list<NewPing> ultrasonics;
int count = 0, triggPin = 0, echoPin = 0;

//variables
float range;
unsigned long range_timer;
float duration, distance;
sensor_msgs::Range range_msg;
 
void setup() {
    while (nh.hasParam("US" << count << "/triggPin") && nh.hasParam("US" << count << "/echoPin")) 
    {
      triggPin = nh.getParam("US" << count << "/triggPin");
      echoPin = nh.getParam("US" << count << "/echoPin");

      pinMode(triggPin, OUTPUT);
      pinMode(echoPin, INPUT);

      parameters.insert(new NewPing(triggPin, echoPin, maxDistance));
    }

    nh.initNode();
    nh.advertise(pub_range_ultrasound);
}

void loop() {
  unsigned long currentMillis = millis();
 
  if (currentMillis-range_timer >= intervalR)
  {
    range_timer = currentMillis+intervalR;
   
    range_msg.range = ultrasonics.ping_cm();
    pub_range_ultrasound.publish(&range_msg);
    }
   
   nh.spinOnce();
}
