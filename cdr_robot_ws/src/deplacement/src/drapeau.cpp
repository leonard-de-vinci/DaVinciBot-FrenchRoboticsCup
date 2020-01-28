#include "ros/ros.h"
#include "std_msgs/Int16.h"
#include "std_msgs/String.h"
#include <wiringPi.h>
//#include <stdio.h>

int global = 1;

void tireCallback(std_msgs::Int16 msg)
{
    global = msg.data;
    ROS_INFO("valeur [%s]",global);
}

int main(int argc, char **argv)
{
    setenv("WIRINGPI_GPIOMEM", "1", 1);
    ros::init(argc, argv, "count_Flag");
    ros::NodeHandle n;
    ros::Publisher flag_pub = n.advertise<std_msgs::Int16>("flagGo", 1000);
    
    ros::Subscriber sub = n.subscribe("PinGo", 1, tireCallback);
    //ros::Subscriber sub2 = n.subscribe("/speedRight", 1, tireCallback);
    
    
    wiringPiSetupGpio();
    pinMode (18, PWM_OUTPUT) ;
    pwmSetMode (PWM_MODE_MS);
    pwmSetRange (2000);
    pwmSetClock (192);
   
  
    ros::Rate loop_rate(10);
    int count = 0;
    std_msgs::Int16 msg;
    while (ros::ok() && msg.data != 1)
    {        
        while (global == 1){
            int wait = 1;
            ROS_INFO("Tire la tirette connard");
            //ros::spinOnce();
        }
        
        double begin = ros::Time::now().toSec();
        double now = ros::Time::now().toSec();
        while (now - begin < 15)
        {
            now = ros::Time::now().toSec();
            msg.data = 0;
            flag_pub.publish(msg);
            ROS_INFO("Waiting");
            
        }
        msg.data = 1;
        flag_pub.publish(msg);
        pwmWrite(18,150);
        delay(1000);
        pwmWrite(18,200);
        ROS_INFO("I'm Done");

        
        loop_rate.sleep();
        ++count;
        
    }
    
    return 0;
}
