#!/usr/bin/env python
import rospy
import time
from bot_coordinates.msg import Coordinates
from std_msgs.msg import Int8
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
    return np.arctan2(np.sin(angle), np.cos(angle))


def coordcallback(msg):
    global rightpub, leftpub, V, K, targetAngle, buffer
    if(buffer%5 == 0):
        alpha = w(w(targetAngle) - w(msg.theta))
	# alpha = alpha *alpha
        Vr = V*(np.cos(alpha)-K*np.sin(alpha))  # rad/s
        Vl = V*(np.cos(alpha)+K*np.sin(alpha))  # rad/s
        msg = Int8()
        msg.data = Vr
        rightpub.publish(msg)
        msg.data = Vl
        leftpub.publish(msg)
        # rospy.loginfo("|| "+str(Vr)+" | "+str(Vl)+" |")
    buffer += 1


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global wheelDiameter, entraxe, wheelRadius, l, K, targetAngle, V
    wheelDiameter = 61.50  # mm
    wheelRadius = wheelDiameter/2
    # entraxe = 160.00  # mm
    # l = 160.00  # mm? not sure
<<<<<<< HEAD
    K = 0.7 # entraxe/(2*l)  # main parameter    K [1/2:1] #! this is the most important param
=======
    K = 0.6 # entraxe/(2*l)  # main parameter    K [1/2:1] #! this is the most important param
>>>>>>> 1d7c349d4b04e4ef8a1c3454278b8713a114119f
    targetAngle = 0.00
    V = 0.00
    global rightpub, leftpub, coordsub, buffer
    buffer = 0
    rospy.init_node("tickviewer", anonymous=False)
    instructionsub = rospy.Subscriber("/control", FloatArr, control_callback)
    coordsub = rospy.Subscriber("/coords", Coordinates, coordcallback)
    rightpub = rospy.Publisher("/N1/target", Int8, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", Int8, queue_size=1)
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()
