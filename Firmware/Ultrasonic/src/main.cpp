#include <ros.h>
#include <sensor_msgs/Range.h>

#define MAXDISTANCE 400         // Max distance allowed to be returned by the sensors
#define INTERVAL_R 200          // Interval between each measurement
#define NUMBER 2                // Number of sensors

u_int sonarIndex = 0;           // Index of the current sensor measuring
unsigned long range_timer;      // Time (in millisecond) from which any sensor can start a new measurement
float duration;                 // Duration of the sensor pulse

int trigs[NUMBER] = {1, 5}; //{1, 5, 7, 16, 20, 22};      // Array of trigger pins for all sensors
int echos[NUMBER] = {2, 4}; //{2, 4, 8, 17, 19, 23};      // Same for echo pins

ros::NodeHandle nh;                             // Object permitting the comunication with ROS

sensor_msgs::Range range_msg;
sensor_msgs::Range range_msg2;
sensor_msgs::Range ranges[NUMBER] = {range_msg, range_msg2};                           // Initializing range messages and getting them in an array

ros::Publisher pub_range_ultrasound("/ultrasound", &range_msg);
ros::Publisher pub_range_ultrasound2("/ultrasound2", &range_msg2);
ros::Publisher publishers[NUMBER] = {pub_range_ultrasound, pub_range_ultrasound2};       // Initializing publishers and getting them in an array

float returnDistance(int i) {               // Return the distance between the sensor number <i> and the nearest object 
  digitalWrite(trigs[i], LOW);              // Next lines triggers a sensor 
  delayMicroseconds(2);
  digitalWrite(trigs[i], HIGH);
  delayMicroseconds(10);
  digitalWrite(trigs[i], LOW);

  duration = pulseIn(echos[i], HIGH);       // Getting the duration of sensor pulse

  return duration/58;                       // Conversion from time to distance (duration/29/2, return centimeters)
}
 
void setup() {

    for (u_int i = 0; i < NUMBER; i++)          // Setting modes for all the sensor's pins
    {
        pinMode(trigs[i], OUTPUT);
        pinMode(echos[i], INPUT);
    }

    nh.initNode();
    
    for (u_int i = 0; i < NUMBER; i++)          // Logging state of connexion between the node and the concerned topics
    {
        nh.advertise(publishers[i]);
    }
}

void loop() {
    unsigned long currentMillis = millis();
 
    if (currentMillis-range_timer >= INTERVAL_R) {              // (interval from previous measure and now >= minimum interval)
        range_timer = currentMillis + INTERVAL_R;

        ranges[sonarIndex].range = returnDistance(sonarIndex);
        publishers[sonarIndex].publish(&ranges[sonarIndex]);          // Publishing sensor's value in the topic with the same number

        ++sonarIndex;                                           // Getting to the next sensor
    }
    
    if (sonarIndex >= NUMBER){                                  // Condition to loop in the pins arrays
        sonarIndex = 0;
    }

    nh.spinOnce();
}
