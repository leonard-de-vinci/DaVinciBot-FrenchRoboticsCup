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
    global rightpub, leftpub, V, K, targetAngle, buffer, Kd, dalpha
    if(buffer % 5 == 0):
        alpha = w(w(targetAngle) - w(msg.theta))
        dalpha = w(dalpha - alpha)
        Vr = V*(np.cos(alpha)+(K*np.sin(alpha)+Kd*np.sin(dalpha)))  # rad/s
        Vl = V*(np.cos(alpha)-(K*np.sin(alpha)+Kd*np.sin(dalpha)))  # rad/s
        dalpha = alpha  # so we don t need an old error
        msg = Int8()
        msg.data = Vr
        rightpub.publish(msg)
        msg.data = Vl
        leftpub.publish(msg)
        # rospy.loginfo("|| "+str(Vr)+" | "+str(Vl)+" |")
    buffer += 1


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global K, targetAngle, V, dalpha, Kd
    dalpha = np.pi  # ! might need some tweeks
    K = 1.0  # entraxe/(2*l)  # main parameter    K [1/2:1] #! this is the most important param
    Kd = 0.3  # wheight for derror                          #! this param i simportant too now
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
