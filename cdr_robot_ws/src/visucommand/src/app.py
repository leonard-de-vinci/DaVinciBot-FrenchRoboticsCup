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
    found = False
    for i in range(len(arr)):
        if arr[i].sender == msg.sender:
            arr[i] = msg
            found = True
    if not found:
        arr.append(msg)
    for i in range(100):
        print()
    for j in range(5):
        temp = ""
        for i in arr:
            temp += " "
            temp += i.sender[j]
        print(temp)
    temp = ""
    for i in arr:
        temp += " "
        temp += "-"
        print(temp)
    for j in range(5):
        temp = ""
        for i in arr:
            temp += " "
            temp += i.destination[j]
        print(temp)
    temp = ""
    for i in arr:
        temp += " "
        temp += str(i.order)
    print(temp)
    print()
    temp = ""
    for i in arr:
        temp += " "
        temp += str(i.precision)
    print(temp)


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
