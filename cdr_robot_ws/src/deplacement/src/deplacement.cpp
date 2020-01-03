#include "ros/ros.h"
#include "std_msgs/String.h"
#include <sstream>
#include <wiringPi.h>
#include "std_msgs/Int16.h"

int main(int argc, char **argv)
{
  ros::init(argc, argv, "deplacement robot");
  ros::NodeHandle n;
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  ros::Publisher pub_right = n.advertise<std_msgs::Int16>("/robot/wheel/left", 1000);
  ros::Publisher pub_left = n.advertise<std_msgs::Int16>("/robot/wheel/right", 1000);
  
  ros::Rate loop_rate(10);
  int count = 0;
  
  wiringPiSetup();
  while (ros::ok())
  {
    std_msgs::String msg;
    std::stringstream ss;
    ss << "hello world " << count;
    msg.data = ss.str();

    ROS_INFO("%s", msg.data.c_str());
    chatter_pub.publish(msg);
    ros::spinOnce();
    loop_rate.sleep();
    ++count;
  }
  return 0;
}