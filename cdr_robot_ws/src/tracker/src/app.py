#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from message_filters import ApproximateTimeSynchronizer
from message_filters import Subscriber
import numpy as np
import sys
import signal


def signal_handler(signal, frame):
  rospy.signal_shutdown("manual stop")#gracefully shutdown
  sys.exit(0)


def updatepos(rightmsg,leftmsg):
    global entraxe , X , Y , theta , coordpub , wheelRadius
    Vr = ttomm(rightmsg.ticks)/0.01#rot/s
    Vl = ttomm(leftmsg.ticks)/0.01#rot/s
    V = wheelRadius*(Vr+Vl)/2.0#mm*rot/s
    thetadot = np.pi*2.00*wheelRadius*(Vr-Vl)/entraxe#rad/s
    theta+=thetadot#rad
    Xdot = np.cos(theta)*V
    Ydot = np.sin(theta)*V
    X+=Xdot
    Y+=Ydot
    rospy.loginfo("| "+str(Xdot)+" "+str(Ydot)+" "+str(thetadot)+" |")
    pload = Coordinates()
    pload.x=X
    pload.y=Y
    pload.theta = theta
    pload.xdot = Xdot 
    pload.ydot = Ydot 
    pload.thetadot = thetadot
    coordpub.publish(pload)

def ttomm(ticks):
    global wheelDiameter, Nticks
    #distanceoneturn = np.pi*wheelDiameter #mm
    return (ticks/Nticks)#*distanceoneturn #rot

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    global X,Y,theta
    X =0.0#mm
    Y =0.0#mm
    theta =0.0 #? rad not sure 
    global wheelDiameter,entraxe,Nticks,wheelRadius
    Nticks = 1024.00#ticks
    entraxe = 160.00#mm
    wheelDiameter = 69.00#mm
    wheelRadius = wheelDiameter/2.0#mm
    global coordpub,rightsub,leftsub
    rightsub = Subscriber("/right/reality",IntArr)
    leftsub = Subscriber("/left/reality",IntArr)
    q = 3#buffer queu size
    deltaT = 0.005# time interval for sync in s
    timesync = ApproximateTimeSynchronizer([rightsub,leftsub],q,deltaT,allow_headerless=True)#time sync to sync right with left
    timesync.registerCallback(updatepos)
    coordpub = rospy.Publisher("/coords",Coordinates,queue_size=3)
    rospy.init_node("rospy_tracker",anonymous=False)
    rospy.loginfo("> tracker succesfully initialised")
    rospy.spin()# while true for ros