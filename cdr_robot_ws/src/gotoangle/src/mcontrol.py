#!/usr/bin/env python
import rospy
import time
from bot_coordinates.msg import Coordinates
from std_msgs.msg import Int8
from PID.msg import FloatArr
from bot_coordinates.msg import move
from bot_coordinates.msg import command
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def targetCallback(msg):
    global V, targettheta, K, A, buffer
    targettheta = w(msg.angle)
    V = msg.V
    K = msg.K
    A = msg.A
    buffer = 0


def commandCallback(msg):
    global me, state, precision
    if msg.destination == me:
        state = msg.order
        precision = msg.precision


def w(angle):
    return np.arctan2(np.sin(angle), np.cos(angle))


def coordCallback(msg):
    global rightpub, leftpub, V, K, A, targettheta, buffer, state
    if state == 1:  # point forward steering controler
        if(buffer >= precision):
            buffer = 0
            (Vr, Vl) = (0, 0)  # init for default values
            alpha = w(w(targetAngle) - w(msg.theta))
            Vr = V*(A*np.cos(alpha)-K*np.sin(alpha))  # rad/s
            Vl = V*(A*np.cos(alpha)+K*np.sin(alpha))  # rad/s
            msg = Int8()
            msg.data = Vr
            rightpub.publish(msg)
            msg.data = Vl
            leftpub.publish(msg)
        buffer += 1
    elif state == 2:  # rotation translation speeds
        if(buffer >= precision):
            buffer = 0
            entraxe = 290.00  # mm
            wheelRadius = 61.5/2.0  # mm
            Vr = (2*V+A*entraxe)/(2*wheelRadius)
            Vl = (2*V-A*entraxe)/(2*wheelRadius)
            msg = Int8()
            msg.data = Vr
            rightpub.publish(msg)
            msg.data = Vl
            leftpub.publish(msg)
        buffer += 1


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global targettheta, theta, V, K, A, state, me, precision, buffer
    global coordsub, rightpub, leftpub, targetsub, commandsub
    state = 0
    buffer = 0
    precision = 0
    theta = 0
    targettheta = 0
    me = "mcontrol"
    rospy.init_node("mcontrol", anonymous=False)
    targetsub = rospy.Subscriber("/movement", move, targetCallback)
    commandsub = rospy.Subscriber("/control", command, commandCallback)
    coordsub = rospy.Subscriber("/coords", Coordinates, coordCallback)
    rightpub = rospy.Publisher("/N1/target", Int8, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", Int8, queue_size=1)
    rospy.loginfo("> mcontrol succesfully initialised")
    rospy.spin()
