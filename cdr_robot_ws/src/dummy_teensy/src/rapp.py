#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr
import numpy as np #pylint ignore
import time
import signal
import sys

def target_callback(msg):
    global dtarget,dcycles
    dtarget = msg.ticks
    dcycles = msg.cycles
    rospy.loginfo("-_-_-_-_-_-_-_-_-_-_-_-_-_-")

def break_callback(msg):
    global breakstate
    breakstate = msg.data

def p(x):
    A=0.6093
    B = 2.794
    C = 99.69
    a = 1
    b = 30.04
    c = 390
    d = 2080
    return ((A*x*x)+(B*x)+C)/((a*x*x*x)+(b*x*x)+(c*x)+d)

def setup():
    global dtarget,dval,dcycles,breakstate
    running = True
    dval =0
    dtarget=5
    dcycles=10000
    breakstate = False
    global realitypub,targetsub,breaksub
    realitypub = rospy.Publisher("/N2/reality",IntArr)
    targetsub = rospy.Subscriber("/N2/target",IntArr,target_callback)
    breaksub = rospy.Subscriber("/breakServo",Bool,break_callback)
    rospy.init_node("dummy_rightteensy",anonymous=False)
    rospy.loginfo("> succesfully initialised")
    while running:
        if(not breakstate):
            if dcycles>0:
                dcycles-=1
                noise = np.random.randint(-2,2)
                dval = (8*dval+2*dtarget+noise)/10
                msg = IntArr()
                msg.ticks = dval
                msg.cycles = dcycles
                realitypub.publish(msg)
                rospy.loginfo("ticks: "+str(msg.ticks)+ " ||  cycles: "+str(msg.cycles))
            else:
                rospy.loginfo("cycles empty")
        else:
            rospy.loginfo("____breaking____")
        time.sleep(0.01)

def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    setup()