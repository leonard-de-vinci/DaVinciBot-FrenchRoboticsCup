#include <ros.h>
#include <std_msgs/Int32MultiArray.h>

#define MAXDISTANCE 400         // Max distance allowed to be returned by the sensors
#define INTERVAL_R 200          // Interval between each measurement
#define NUMBER 2                // Number of sensors

u_int sonarIndex = 0;           // Index of the current sensor measuring
unsigned long range_timer;      // Time (in millisecond) from which any sensor can start a new measurement
float duration;                 // Duration of the sensor pulse

int trigs[NUMBER] = {1, 7}; //{1, 5, 7, 16, 20, 22};      // Array of trigger pins for all sensors
int echos[NUMBER] = {2, 8}; //{2, 4, 8, 17, 19, 23};      // Same for echo pins

ros::NodeHandle nh;                             // Object permitting the comunication with ROS

std_msgs::Int32MultiArray sensorsValues;      // Array of the values from all the sensors

ros::Publisher publisher("/ultrasound", &sensorsValues);   //

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
    sensorsValues.data_length = NUMBER;         // Initializing the data array and length
    sensorsValues.data = new int32_t[NUMBER];

    for (u_int i = 0; i < NUMBER; i++)          // Setting modes for all the sensor's pins
    {
        pinMode(trigs[i], OUTPUT);
        pinMode(echos[i], INPUT);
    }

    nh.initNode();

    nh.advertise(publisher);    // Initializing publisher 
}

void loop() {
    unsigned long currentMillis = millis();
 
    if (currentMillis-range_timer >= INTERVAL_R) {                              // (interval from previous measure and now >= minimum interval)
        range_timer = currentMillis + INTERVAL_R;                               // Updating the delay before the next measure

        sensorsValues.data[sonarIndex] = round(returnDistance(sonarIndex));     // Updating the array with a new measure
        publisher.publish(&sensorsValues);                                      // Publishing the updated array
        ++sonarIndex;                                                           // Getting to the next sensor
    }
    
    if (sonarIndex >= NUMBER){                                                  // Condition to loop in the pins arrays without getting out of index
        sonarIndex = 0;
    }

    nh.spinOnce();
}
