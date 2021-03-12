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
    #Mis arbitrairement le temps de l'implementation dans "Centralized", il faudra récupérer les coordonnées callback
    XY = np.array([1.5,1])
    
    vectors_sum = np.array([0.0,0.0])
    for i in range(len(ranges)):
        if ranges[i] < 2.00 and ranges[i]>0.06 :
            if i*laser_scan.angle_increment < np.pi/2.0 and i*laser_scan.angle_increment > np.pi/2.0 :
                angle = ((double)i*laser_scan.angle_increment-0.0) *(laser_scan.angle_max-laser_scan.angle_min)/(len(ranges) -0) + laser_scan.angle_min
                temp = np.array([XY[0] + (1/ranges[i]**2)*np.cos(angle),XY[1] + (1/ranges[i]**2)*np.sin(angle)])
                

            #rospy.loginfo(str(ranges[i]))
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


    #Je stock juste ça là comme ça 
    # wall_top_XY = np.array([XY[0],(float)(0)])
    # wall_bot_XY = np.array([XY[0],(float)(2)])
    # wall_right_XY = np.array((float)(3),XY[1]) 
    # wall_left_XY = np.array((float)(0),XY[1])
    

    # test = False
    # for i in range(len(ranges)):
    #     if ranges[i] < 1.00 and ranges[i]>0.06 and i*laser_scan.angle_increment < (float)(3.14159265359) and i*laser_scan.angle_increment > (float)(0):
    #         test = True
    #         rospy.loginfo(str(ranges[i]))
    # if test:
    #     buffer += 1
    # else:
    #     buffer -= 1
    # if buffer < 0:
    #     buffer = 0
    # if buffer > 10:
    #     precision = -1
    # rospy.loginfo("breaking!!")
    # if buffer > 20:
    #     buffer = 20
    # rospy.loginfo(str(test))

if __name__ == '__main__':
    
    Lidar_setup()
    rospy.spin()


