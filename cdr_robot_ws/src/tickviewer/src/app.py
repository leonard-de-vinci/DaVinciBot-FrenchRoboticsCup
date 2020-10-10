#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
import matplotlib.pyplot as plt

def reality_callback(msg):
    global ylist,xlist,ytarget,xneg
    ylist.append(msg.ticks)
    xlist.append(xneg-msg.cycles)

def target_callback(msg):
    global ytarget,ylist,xlist,xneg
    ylist=[]
    xlist=[]
    ytarget = msg.ticks
    xneg = msg.cycles

def display():
    global ytarget,ylist,xlist
    plt.cla()
    plt.plot(xlist,ylist)
    plt.ylabel('ticks')
    plt.xlabel('cycles')
    plt.draw()
    plt.pause(0.01)

def main():
    running = True

    global ylist,xlist,ytarget,xneg
    xlist=[]
    ylist=[]
    xneg=100
    ytarget=0
    global targetsub,realitysub
    realitysub = rospy.Subscriber("/right/reality",IntArr,reality_callback)
    targetsub = rospy.Subscriber("/right/target",IntArr,reality_callback)
    rospy.init_node("tickviewer", anonymous=False)
    rospy.loginfo("> viewer correctly initialised")
    display()
    try:
        while running:
            time.sleep(0.5)
            display()
    except KeyboardInterrupt:
        rospy.loginfo("we out boys")
        


if __name__ == '__main__':
    plt.ion()
    main()