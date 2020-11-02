#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from PID.msg import FloatArr
import signal
import sys
import numpy as np

def signal_handler(signal, frame):
  sys.exit(0)

def control_callback(msg):
    global V , targetAngle
    targetAngle = w(msg.theta)
    V = msg.v

def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    #alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha

def coordcallback(msg):
    global rightpub, leftpub , V , K, targetAngle, buffer
    if(buffer%10==0):
        alpha = w(targetAngle) - w(msg.theta)
        alpha = w(alpha)
        Vr = V*(np.cos(alpha)+K*np.sin(alpha))  #rad/s
        Vl = V*(np.cos(alpha)-K*np.sin(alpha))  #rad/s
        msg = IntArr()
        msg.cycles = 1000
        msg.ticks = Vr
        rightpub.publish(msg)
        msg.ticks = Vl
        leftpub.publish(msg)
        rospy.loginfo("|| "+str(Vr)+" | "+str(Vl)+" |")
    buffer+=1

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global wheelDiameter, entraxe , wheelRadius , l ,K , targetAngle , V
    wheelDiameter = 69.00#mm
    wheelRadius = wheelDiameter/2
    entraxe = 160.00#mm
    l = 160.00#mm? not sure
    K = entraxe/(2*l)#main parameter
    targetAngle = 1
    V = 10.00#mm/s
    global rightpub , leftpub , coordsub , buffer
    buffer = 0
    rospy.init_node("tickviewer", anonymous=False)
    instructionsub = rospy.Subscriber("/control",FloatArr,control_callback)
    coordsub = rospy.Subscriber("/coords",Coordinates,coordcallback) 
    rightpub = rospy.Publisher("/N1/target",IntArr,queue_size=1)
    leftpub = rospy.Publisher("/N2/target",IntArr,queue_size=1)
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()