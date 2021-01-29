#!/usr/bin/env python
import rospy
import time
from PID.msg import FloatArr
from std_msgs.msg import Bool
from bot_coordinates.msg import command
from std_msgs.msg import Int8
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def commandCallback(msg):
    global blocked, waiting, sender, state
    if blocked:
        if waiting == msg.order and sender = msg.sender:
            blocked = False
            state += 1
    else:
        pass
        # TODOimplement the state machine here


def waypointCallback(msg):
    pass


def mainloop():
    if state == 0:
        # turn of the mcontrol
        commsg = command()
        commsg.sender = me
        commsg.destination = "mcontrol"
        commsg.order = 0
        commsg.precision = 0
        # trun off the gotogoal
        commsg = command()
        commsg.sender = me
        commsg.destination = "gotogoal"
        commsg.order = 0
        commsg.precision = 0
        state += 1
    if state == 1:
        # TODO : wait for the start
        pass
        state += 1
    if state == 2:
        pass
        # TODO iterate threw the orders


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    # ##---------------------waypoints and stuff
    global waypoints
    waypoints = np.array([0, 0])
    # ##---------------------logique
    global blocked, waiting, sender, me, precision, order, state
    blocked = False
    waiting = 0  # what we waiting for
    sender = "null"  # from whom are we waiting a message
    me = "brain"
    precision = 0
    order = 0
    state = 0

    # ##---------------------ROS
    global emergencystop, commandpub, commandsub, waypointpub, guisub
    rospy.init_node("thebrain", anonymous=False)
    emergencystop = rospy.Publisher("/breakServo", Bool, queue_size=1)
    commandpub = rospy.Publisher("/control", command, queue_size=1)
    commandsub = rospy.Subscriber("/control", command, commandCallback)
    waypointpub = rospy.Publisher("/movement", move, queue_size=1)
    guisub = rospy.Subscriber("/waypoints", waypointlist, waypointCallback)
    rospy.spin()
