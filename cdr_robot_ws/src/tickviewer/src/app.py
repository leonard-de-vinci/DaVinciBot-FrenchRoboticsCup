#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
import matplotlib.pyplot as plt
import numpy
plt.ion()

def reality_callback(msg):
    global ylist,xlist,ytarget,xneg
    ylist.append(msg.ticks)
    xlist.append(xneg-msg.cycles)
    #rospy.loginfo("___new values___")

def target_callback(msg):
    global ytarget,ylist,xlist,xneg
    ylist=[]
    xlist=[]
    ytarget = msg.ticks
    xneg = msg.cycles

def display():
    global ytarget,ylist,xlist,theaxis
    theaxis.clear()
    theaxis.plot(xlist,ylist,ylabel="ticks",xlabel="cycles")
    theaxis.legend()
    plt.draw()
    plt.pause(0.001)

def main():
    running = True

    global ylist,xlist,ytarget,xneg,theaxis
    fig = plt.figure()
    cfg = fig.add_gridspec(1,1)
    theaxis = fig.add_subplot(cfg[0, 0])
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
            display()
            time.sleep(0.05)
    except KeyboardInterrupt:
        rospy.loginfo("we out boys")
        


if __name__ == '__main__':
    main()