#!/usr/bin/env python
import rospy
import time
from PID.msg import FloatArr
from std_msgs.msg import Int8
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def control_callback(msg):
    global V, angular, entraxe, wheelRadius, rightpub, leftpub
    angular = msg.theta
    V = msg.v
    Vr = (2*V+angular*entraxe)/(2*wheelRadius)
    Vl = (2*V-angular*entraxe)/(2*wheelRadius)
    pload = Int8()
    pload.data = Vr
    rightpub.publish(pload)
    pload.data = vl
    leftpub.publish(pload)


def w(angle):
    return np.arctan2(np.sin(angle), np.cos(angle))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global wheelDiameter, entraxe, wheelRadius, K, angular, V
    wheelDiameter = 69.00  # mm
    wheelRadius = wheelDiameter/2.0
    entraxe = 160.00  # mm
    angular = 0
    targetAngle = 0.00
    V = 0.00
    global rightpub, leftpub, coordsub, buffer
    buffer = 0
    rospy.init_node("tickviewer", anonymous=False)
    instructionsub = rospy.Subscriber("/control", FloatArr, control_callback)
    rightpub = rospy.Publisher("/N1/target", Int8, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", Int8, queue_size=1)
    rospy.loginfo("> translation rotation node initialised")
    rospy.spin()
