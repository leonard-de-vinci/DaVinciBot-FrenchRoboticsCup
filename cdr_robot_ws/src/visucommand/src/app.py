#!/usr/bin/env python
import rospy
import time
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from bot_coordinates.msg import movement
from bot_coordinates.msg import move
from bot_coordinates.msg import target
from bot_coordinates.msg import command
from sensor_msgs.msg import LaserScan
from PID.msg import FloatArr
from std_msgs.msg import Int32
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def commandCallback(msg):
    global arr
    if len(arr) > 10:
        arr.pop()
    else:
        arr.append(msg)
    for i in arr:
        print(msg.sender + " --> " + msg.destination + "    " + msg.order + " : "+msg.precision)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global arr
    arr = []
    # ##---------------------ROS
    rospy.init_node("visuControl", anonymous=False)
    global commandsub, movementpub, lidarsub, emergencypub
    commandsub = rospy.Subscriber("/control", command, commandCallback)
    rospy.loginfo(">  center succesfully initialised")
    rospy.spin()
