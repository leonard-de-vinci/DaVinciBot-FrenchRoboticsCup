#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int16.h"

int global = 1;

void chatterCallback(std_msgs::Int16 msg)
{
  global = msg.data;
  ROS_INFO("I heard: %i", global);
}

bool begin()
{
  bool letsgo = (global == 0);
  return letsgo;
}


int main(int argc, char **argv)
{
  ros::init(argc, argv, "drapo");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("PinGo", 1000, chatterCallback);
  ros::Rate r(10);
  bool go = begin();
 
  while(go == false){
     go = begin();
     ros::spinOnce();
     r.sleep();
  }
  ROS_INFO("C'est good");
  return 0;
}
