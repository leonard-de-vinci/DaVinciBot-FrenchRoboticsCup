#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include "std_msgs/String.h"
#include <wiringPi.h>
#include <stdio.h>
#include <errno.h>
#include <string.h>

const int pwmPin = 23; // PWM LED - Broadcom pin 18, P1 pin 12

int pwmValue = 0; // Use this to set an LED brightness

int main(int argc, char **argv) {
    setenv("WIRINGPI_GPIOMEM", "1", 1);
    ros::init(argc, argv, "Servo");
    ros::NodeHandle n;
    wiringPiSetupGpio(); // Initialize wiringPi -- using Broadcom pin numbers
    pinMode(pwmPin, PWM_OUTPUT); // Set PWM LED as PWM output

   int count = 0;
   while(1)
   {
   pwmWrite(pwmPin, pwmValue); // Entre 0 et 1024
   }
    while(count < 1000){
        count++;
    }
    return 0;
}
