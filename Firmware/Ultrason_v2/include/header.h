#include <vector>
#include <ros.h>
#include <PID/IntArr.h>
#include "ultra.cpp"

// classes
// Sensor(id, triggerPin, echoPin);
std::vector<Sensor> sensorsList = {Sensor(14,15), Sensor(16,17), Sensor(18,19), Sensor(20,21), Sensor(22,23)};

//ros global
ros::NodeHandle nh;
#define TOPIC_ULTRASOUND "/ultrasound"
PID::IntArr sensorData;
ros::Publisher publisher(TOPIC_ULTRASOUND, &sensorData);