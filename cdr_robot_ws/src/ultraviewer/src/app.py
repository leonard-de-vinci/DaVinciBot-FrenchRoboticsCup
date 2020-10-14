#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
import matplotlib.pyplot as plt
import signal
import sys
import numpy as np
plt.ion()

def ultrasound_callback(msg):
    global xlist,theaxis
    xlist[msg.cycles]=msg.ticks
    rospy.loginfo(">> received !!")

def display():
    global xlist,theaxis
    theaxis.clear()
    theaxis.bar(range(5),xlist)
    plt.draw()
    plt.pause(0.001)

def main():
    running = True

    global xlist,theaxis
    theaxis = plt.axes()
    xlist=[0,0,0,0,0]
    distsub = rospy.Subscriber("/ultrasound",IntArr,ultrasound_callback)
    rospy.init_node("ultraviewer", anonymous=False)
    rospy.loginfo("> viewer correctly initialised")
    display()
    while running:
        display()
        time.sleep(0.05)
        
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    main()