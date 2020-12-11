#!/usr/bin/env python
import rospy 
import time
from PID.msg import speed
from bot_coordinates.msg import Coordinates
from PID.msg import FloatArr
from std_msgs.msg import Bool
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global rightpub, leftpub
    rospy.init_node("tster", anonymous=False)
    breakpub = rospy.Publisher("/breakServo", Bool, queue_size=1)
    leftpub = rospy.Publisher("/N2/target", speed, queue_size=2)
    print("waiting for full init")
    time.sleep(5)
    msg = speed()
    msg.dir = True
    msg.ticks = 0
    leftpub.publish(msg)
    bmsg = Bool()
    bmsg.data = False
    breakpub.publish(bmsg)
    print("ON TEST BENCH")
    print("test for motor connectivity")
    print("when ready press enter:")
    while True:
        msg.dir = True
        msg.ticks = 30
        leftpub.publish(msg)
        time.sleep(0.2)
        print("--------------------------------------------")
        print("LEFT FORWARD")
        time.sleep(3)
        msg.dir = False
        msg.ticks = 30
        leftpub.publish(msg)
        time.sleep(0.2)
        print("--------------------------------------------")
        print("LEFT BACKWARD")
        time.sleep(3)