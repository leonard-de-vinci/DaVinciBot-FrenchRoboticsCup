#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Int16.h"

int global = 0;

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
  ros::Publisher flag_pub = n.advertise<std_msgs::Int16>("flagGo", 1000);

  ros::Rate r(10);
  bool go = begin();
 
  while(go == false){
     go = begin();
     ros::spinOnce();
     r.sleep();
  ROS_INFO("j'attends");

  }

  double begin = ros::Time::now().toSec();
  double now = ros::Time::now().toSec();

  std_msgs::Int16 msg_servo;
  msg_servo.data = 0;

  while(now - begin < 95)
  {
    now = ros::Time::now().toSec();
    //flag_pub.publish(msg_servo);
  }
  begin = ros::Time::now().toSec();
  now = ros::Time::now().toSec();

  msg_servo.data = 1;

  while(now - begin < 5)
  {
    now = ros::Time::now().toSec();
    flag_pub.publish(msg_servo);
  }
  
  msg_servo.data = 0;
  flag_pub.publish(msg_servo);
  ROS_INFO("C'est good");
  return 0;
}
