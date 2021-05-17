#!/usr/bin/env python3

import rospy
import numpy as np
#from PID.msg import IntArr
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
from bot_coordinates.msg import Coordinates
bot_coords = np.array([0.0,0.0,0.0])



def Lidar_setup():
    global lidar_pub, lidarsub
    #buffer = 0
    rospy.init_node('Lidar')
    lidarsub = rospy.Subscriber("/scan", LaserScan, Lidar_usings)
    coords_sub = rospy.Subscriber("/coords", Coordinates, coords_callback)
    lidar_pub = rospy.Publisher('/resultant_lidar', Coordinates)
    rospy.loginfo("Le node Lidar a demarre correctement")

def coords_callback(msg):
    global bot_coords
    bot_coords[0] = msg.x
    bot_coords[1] = msg.y
    bot_coords[2] = msg.theta


def Lidar_usings(laser_scan):
    global resultXY, lidar_pub, lidarsub, bot_coords
    #rospy.loginfo("lidar hasn t been implemented yet")
    ranges = np.array(laser_scan.ranges)
    vectors_sum = np.array([0.0,0.0])
    #rospy.loginfo(len(laser_scan.ranges))
    mid_angle = (len(laser_scan.ranges)/2.0)*laser_scan.angle_increment
    k = 1 #Coefficient de poids vectoriel
    for i in range(len(laser_scan.ranges)) :
        if (laser_scan.ranges[i] >= 0.05 and (not np.isinf(laser_scan.ranges[i]))) : 
            angle = bot_coords[2] - laser_scan.angle_min - (laser_scan.angle_max - laser_scan.angle_min)*(float(i)/float(len(laser_scan.ranges)))
            pos = np.array([np.cos(angle),np.sin(angle)])
            pos*= laser_scan.ranges[i]
            pos[0] += bot_coords[0]/1000.0
            pos[1] += bot_coords[1]/1000.0
            #rospy.loginfo(pos)
            if(pos[0] >= 0 and pos[1] >= 0 and pos[0]<= 3.0 and pos[1]<= 2.0) : 
                vectors_sum[0] -= (1/(float(laser_scan.ranges[i])**2))*np.cos(angle) 
                vectors_sum[1] -= (1/(float(laser_scan.ranges[i])**2))*np.sin(angle)
            #else  :rospy.loginfo("AHAHAHAHAHH BOlOSS") 

    k_mur = 25
    vectors_sum[0] += k_mur/float((bot_coords[0]/1000.0)**2)
    vectors_sum[0] -= k_mur/float(((3000.0 - bot_coords[0])/1000.0)**2)
    vectors_sum[1] += k_mur/float((bot_coords[1]/1000.0)**2)
    vectors_sum[1] -= k_mur/float(((2000.0- bot_coords[1])/1000.0)**2)
    vectors_sum *= k
    
    resultXY = vectors_sum
    z = Coordinates()
    z.x = vectors_sum[0]
    z.y = vectors_sum[1]
    lidar_pub.publish(z)

if __name__ == '__main__':
    
    Lidar_setup()
    rospy.spin()


