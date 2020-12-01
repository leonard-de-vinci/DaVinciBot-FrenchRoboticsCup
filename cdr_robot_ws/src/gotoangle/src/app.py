#!/usr/bin/env python
import rospy
import time
from PID.msg import speed
from bot_coordinates.msg import Coordinates
from PID.msg import FloatArr
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def control_callback(msg):
    global V, targetAngle
    targetAngle = w(msg.theta)
    V = msg.v


def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    # alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha


def coordcallback(msg):
    global rightpub, leftpub, V, K, targetAngle, buffer
    if((buffer % 10) == 0):
        alpha = w(targetAngle) - w(msg.theta)
        alpha = w(alpha)
        Vr = V*(np.cos(alpha)+K*np.sin(alpha))  # rad/s
        Vl = V*(np.cos(alpha)-K*np.sin(alpha))  # rad/s
        msg = speed()
        msg.ticks = abs(Vr)
        msg.dir = (Vr >= 0)
        rightpub.publish(msg)
        msg.ticks = abs(Vl)
        msg.dir = (Vl >= 0)
        leftpub.publish(msg)
        rospy.loginfo("|| "+str(Vr)+" | "+str(Vl)+" |")
    buffer += 1


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global wheelDiameter, entraxe, wheelRadius, l, K, targetAngle, V
    wheelDiameter = 69.00  # mm
    wheelRadius = wheelDiameter/2
    entraxe = 160.00  # mm
    ll = 160.00  # mm? not sure
    K = entraxe/(2*ll)  # main parameter    K [1/2:1]
    targetAngle = 1
    V = 0.00
    global rightpub, leftpub, coordsub, buffer
    buffer = 0
    rospy.init_node("tickviewer", anonymous=False)
    instructionsub = rospy.Subscriber("/control", FloatArr, control_callback)
    coordsub = rospy.Subscriber("/coords", Coordinates, coordcallback) 
    rightpub = rospy.Publisher("/N1/target", speed, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", speed, queue_size=1)
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()