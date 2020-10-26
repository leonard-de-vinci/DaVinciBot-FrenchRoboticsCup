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
    global ylist,xlist,ytarget,xneg,thelist,it
    ylist.append(msg.ticks)
    xlist.append(xneg-msg.cycles)
    if msg.cycles>0:
        if(it<len(thelist)):
            thelist[it]+=msg.ticks
            thelist[it]*=(generation[0]/(generation[0]+1))
            it+=1
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
    #theaxis.axhline(ytarget,linestyle='--')
    theaxis.plot(xlist,ylist)
    plt.draw()
    plt.pause(0.001)

def main():
    running = True

    global ylist,xlist,ytarget,xneg,theaxis,thelist,it,generation
    it=0
    thelist=np.loadtxt("respons.csv",delimiter=",").tolist()
    generation = np.loadtxt("gen.csv",delimiter=",").tolist()
    theaxis = plt.axes()
    xlist=[]
    ylist=[]
    xneg=100
    ytarget=0
    global targetsub,realitysub
    realitysub = rospy.Subscriber("/right/reality",IntArr,reality_callback)
    targetsub = rospy.Subscriber("/right/target",IntArr,target_callback)
    rospy.init_node("tickviewer", anonymous=False)
    rospy.loginfo("> viewer correctly initialised")
    display()
    while running:
        display()
        time.sleep(0.05)
        if(it>99):
            tmp = np.array(thelist)
            generation[0]+=1
            tmp2 = np.array(generation)
            np.savetxt("respons.csv", tmp, delimiter=",")
            np.savetxt("gen.csv", tmp2, delimiter=",")
            rospy.loginfo("done")
            sys.exit(0)
        
def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


if __name__ == '__main__':
    main()