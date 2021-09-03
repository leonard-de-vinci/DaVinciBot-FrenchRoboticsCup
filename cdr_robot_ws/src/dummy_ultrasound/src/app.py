#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr
import numpy as np #pylint ignore
import time
import signal
import sys

def setup():
    running = True
    ultrapub = rospy.Publisher("/ultrasound",IntArr)
    rospy.init_node("dummy_ultra",anonymous=False)
    rospy.loginfo("> succesfully initialised")
    maxdist = 2000
    distlist = []
    for i in range(5):
        distlist.append(maxdist/2)
    while running:
        for i in range(len(distlist)):
            distlist[i]+= np.random.randint(maxdist*-1/5,maxdist/5)
            distlist[i] = max(0,min(maxdist,distlist[i]))
            msg = IntArr()
            msg.ticks = int(distlist[i])
            msg.cycles = i
            ultrapub.publish(msg)
            time.sleep(0.1)

def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    setup()