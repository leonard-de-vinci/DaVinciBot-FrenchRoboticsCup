#include <NewPing.h>
#include <ros.h>
#include <Arduino.h>
#include <sensor_msgs/Range.h>

//define the constants
#define maxDistance 400
#define intervalR 60

ros::NodeHandle nh;
sensor_msgs::Range range_msg;
ros::Publisher pub_range_ultrasound("/ultrasound", &range_msg);
unsigned int index = 0, triggPin = 0, echoPin = 0;

int paramLength, duetSize = 2; 
int *ptr, *array, **pins;
NewPing *ultrasonics; 

//variables
float range;
unsigned long range_timer;
float duration, distance;

void setup() {
  nh.initNode();
  nh.loginfo("setup");

    while (!nh.connected()) {
        nh.spinOnce();
    }

    if ( nh.getParam("/ultrasonics/length", &paramLength) ) {

      nh.loginfo("Ultrasonic setup (1/2 ok)");
      nh.loginfo(""+paramLength);
      array = (int *)malloc(2 * paramLength * sizeof(int));

      /*
      pins = (int **)malloc(sizeof(int *) * length + sizeof(int) * duetSize * length); // malloc Init of 2D ultrasonics pins
      ptr = (int *)(pins + length); 
      for(int i = 0; i < length; i++) {
          pins[i] = (ptr + duetSize * i); 
      }
      */

      if ( nh.getParam("ultrasonics/pins", array)) {
        nh.loginfo("Ultrasonics setup (2/2 ok)");
        ultrasonics = (NewPing *)malloc(paramLength * sizeof(NewPing));
        // Init 'ultrasonics' from 'array' data
      }
      else {
        nh.logerror("Can't get 'pins' in 'ultrasonics/' param namespace");
      }
    }
    else {
      nh.logerror("Can't get 'length' in 'ultrasonics/' param namespace");
    }

    
    nh.advertise(pub_range_ultrasound);
}

void loop() {
  unsigned long currentMicros = micros();
 
  if (currentMicros-range_timer >= intervalR)
  {
    range_timer = currentMicros + intervalR;
    
    range_msg.range = ultrasonics[index].ping_cm();
    pub_range_ultrasound.publish(&range_msg);
  }

  index = index >= sizeof(ultrasonics) ? 0 : index + 1;
  nh.spinOnce();
}

