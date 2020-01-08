#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <wiringPi.h>
#include "std_msgs/Int16.h"

int main(int argc, char **argv)
{
   setenv("WIRINGPI_GPIOMEM", "1", 1);

  ros::init(argc, argv, "Go");
  ros::NodeHandle n;
  ros::Publisher pin_go_pub = n.advertise<std_msgs::Int16>("PinGo", 1000);
  wiringPiSetup();

  pinMode(0, INPUT); //wiringPi pin 0 is BCM_GPIO 17.
  
  
  ros::Rate loop_rate(10);
  int count = 0;
  
	
  
 
  while (ros::ok())
  {
    std_msgs::Int16 msg;
    
    
    msg.data = digitalRead(0);

    
    pin_go_pub.publish(msg);

    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}
