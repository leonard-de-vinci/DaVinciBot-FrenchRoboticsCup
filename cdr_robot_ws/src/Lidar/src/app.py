#!/usr/bin/env python3

import rospy
import numpy as np
#from PID.msg import IntArr
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool


def Lidar_setup():
    global lidar_publish, buffer
    buffer = 0
    rospy.init_node('Lidar')
    lidar_publish = rospy.Publisher("breakServo",Bool,queue_size=1)
    sub = rospy.Subscriber('/scan',LaserScan,Lidar_usings)
    rospy.loginfo("Le node Lidar a demarre correctement")


def Lidar_usings(laser_scan):
    #angle_increment = laser_scan.angle_increment
    global buffer, lidar_publish
    ranges = np.array(laser_scan.ranges)
    test = False
    for i in range(len(ranges)):
        if ranges[i] < 1.00 and ranges[i]>0.06 :
            test = True
            rospy.loginfo(str(ranges[i]))
    if test == True :
    	buffer+= 1
    else :
    	buffer -= 1
    if buffer <0:
    	buffer = 0
    if buffer > 10 :
    	msg = Bool()
    	msg.data = True
    	lidar_publish.publish(msg)
        #rospy.loginfo("breaking!!")
    else :
    	msg = Bool()
    	msg.data = False
    	lidar_publish.publish(msg)
    if buffer >20 :
    	buffer = 20
    rospy.loginfo(str(test))
    #rospy.loginfo(str(laser_scan.range_min))
    #if laser_scan.range_min <1.0 :
    #	msg = Bool()
    #	msg.data = True
    #	lidar_publish.publish(msg)
    #else:
    #	msg = Bool()
    #	msg.data = False
    #	lidar_publish.publish(msg)

if __name__ == '__main__':
    
    Lidar_setup()
    rospy.spin()


