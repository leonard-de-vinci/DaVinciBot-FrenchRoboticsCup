#!/usr/bin/env python3

import rospy
#from PID.msg import IntArr
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool


def Lidar_setup():
    lidar_publish = rospy.Publisher('Lidar_validation',Bool,queue_size=1)
    rospy.Subscriber('/scan',LaserScan,Lidar_usings)
    rospy.init_node('Lidar')
    rospy.loginfo("> coucou")
    
   


def Lidar_usings(laser_scan):
    #angle_increment = laser_scan.angle_increment
    print(laser_scan)
    if laser_scan.range_min <= 0.01 :
        lidar_publish.publish(False)


if __name__ == '__main__':
    Lidar_setup()


