#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Bool
from std_msgs.msg import Int8
from bot_coordinates.msg import Coordinates
from message_filters import ApproximateTimeSynchronizer
from message_filters import Subscriber
import numpy as np
import sys
import signal
import time


def signal_handler(signal, frame):
    rospy.signal_shutdown("manual stop")  # gracefully shutdown
    sys.exit(0)


def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    # alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha


def ttomm(ticks):
    global wheelDiameter, Nticks
    return (ticks/Nticks)  # *distanceoneturn #rot


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    global X, Y, theta
    X = 1500.0  # mm
    Y = 1000.0  # mm
    theta = 0.0  # ? rad not sure
    global wheelDiameter, entraxe, Nticks, wheelRadius
    Nticks = 1024.00  # ticks
    entraxe = 275.00  # mm
    wheelDiameter = 61.00  # mm
    wheelRadius = wheelDiameter/2.0  # mm
    global coordpub, rightsub, leftsub
    rospy.init_node("rospy_tracker", anonymous=False)
    rightsub = Subscriber("/N2/reality", Int8)
    leftsub = Subscriber("/N1/reality", Int8)
    q = 3  # buffer queu size
    deltaT = 0.005  # time interval for sync in s
    timesync = ApproximateTimeSynchronizer([rightsub, leftsub], q, deltaT, allow_headerless=True)  # time sync to sync right with left
    timesync.registerCallback(updatepos)
    coordpub = rospy.Publisher("/coords", Coordinates, queue_size=3)
    rospy.loginfo("> tracker succesfully initialised")
    while True:
        pload = Coordinates()
        pload.x = X
        pload.y = Y
        pload.theta = w(theta)
        pload.xdot = Xdot
        pload.ydot = Ydot
        pload.thetadot = thetadot
        coordpub.publish(pload)
        time.sleep(1)
