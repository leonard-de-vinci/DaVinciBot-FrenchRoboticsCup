#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
import matplotlib.pyplot as plt
import signal
import sys
import numpy as np
plt.ion()

def reality_callback(msg):
    global ylist,xlist,ytarget,xneg
    ylist.append(msg.ticks)
    xlist.append(xneg-msg.cycles)
    if(len(ylist)>1000):
        ylist.pop(0)
        xlist.pop(0)
    #rospy.loginfo("___new values___")

def target_callback(msg):
    global ytarget,ylist,xlist,xneg,theaxis
    ylist=[]
    xlist=[]
    ytarget = msg.ticks
    xneg = msg.cycles
    rospy.loginfo(">> reset ")

def display():
    global ytarget,ylist,xlist,theaxis
    theaxis.clear()
    theaxis.axhline(ytarget,linestyle='--')
    if(len(xlist)==len(ylist)):
        theaxis.plot(xlist,ylist)
    else:
        print("length matching ERROR")
    plt.draw()
    plt.pause(0.001)

def main():
    running = True

    global ylist,xlist,ytarget,xneg,theaxis
    theaxis = plt.axes()
    xlist=[]
    ylist=[]
    xneg=100
    ytarget=0
    global targetsub,realitysub
    realitysub = rospy.Subscriber("/N1/reality",IntArr,reality_callback)
    targetsub = rospy.Subscriber("/N1/target",IntArr,target_callback)
    rospy.init_node("tickviewer", anonymous=False)
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