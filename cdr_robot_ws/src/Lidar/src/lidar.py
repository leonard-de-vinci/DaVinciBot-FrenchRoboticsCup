#!/usr/bin/env python3

from PID.msg import IntArr
from Sensor.msg import LaserScan
from std_msgs.msg import Bool


def Lidar_setup():
    lidar_publish = rospy.Publisher('Lidar',Bool,queue=False)
    rospy.init_node()
    rospy.Subscriber('/scan',LaserScan,Lidar_usings)
   


def Lidar_usings(laser_scan):
    #angle_increment = laser_scan.angle_increment
    print(laser_scan)
    if laser_scan.range_min <= 0.01 :
        lidar_publish.publish(False)

if __name__ == '__main__':
    t

