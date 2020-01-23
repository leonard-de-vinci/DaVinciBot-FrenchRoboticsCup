#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include "std_msgs/String.h"

int global = 0;

void tireCallback(std_msgs::Int16 msg)
{
    global = msg.data;
}

int main(int argc, char **argv)
{

    ros::init(argc, argv, "count_Flag");
    ros::NodeHandle n;
    ros::Publisher flag_pub = n.advertise<std_msgs::Int16>("flagGo", 1000);
    
    ros::Subscriber sub = n.subscribe("PinGo", 1000, tireCallback);

    ros::Rate loop_rate(10);
    int count = 0;
    std_msgs::Int16 msg;
    while (ros::ok() && msg.data != 1)
    {
        
        
        while (global == 0){
            int wait = 1;
        }
        
        double begin = ros::Time::now().toSec();
        double now = ros::Time::now().toSec();
        while (now - begin < 95)
        {
            now = ros::Time::now().toSec();
            msg.data = 0;
            flag_pub.publish(msg);
            ROS_INFO("Waiting");
            
        }
        msg.data = 1;
        flag_pub.publish(msg);
        ROS_INFO("I'm Done");

        //ros::spinOnce();
        loop_rate.sleep();
        ++count;
        
    }
    return 0;
}
