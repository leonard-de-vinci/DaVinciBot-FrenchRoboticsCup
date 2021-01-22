#!/usr/bin/env python3

import rospy
import numpy as np
#from PID.msg import IntArr
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool


def Lidar_setup():
    
    rospy.init_node('Lidar')
    global lidar_publish = rospy.Publisher('Lidar_validation',Bool,queue_size=1)
    sub = rospy.Subscriber('/scan',LaserScan,Lidar_usings)
    
    rospy.loginfo("Le node Lidar a démarré correctement")
    
   


def Lidar_usings(laser_scan):
    #angle_increment = laser_scan.angle_increment
    ranges = np.array(laser_scan.range)
    test = True
    for i in range(len(ranges)):
        if ranges[i] < 0.10 :
            test = False
            lidar_publish.publish(test)



if __name__ == '__main__':
    
    Lidar_setup()
    rospy.spin()


