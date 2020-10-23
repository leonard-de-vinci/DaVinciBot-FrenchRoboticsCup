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

def setup():
    global dtarget,dval,dcycles,breakstate
    running = True
    dval =0
    dtarget=100
    dcycles=1000
    breakstate = False
    global realitypub,targetsub,breaksub
    realitypub = rospy.Publisher("/right/reality",IntArr)
    targetsub = rospy.Subscriber("/right/target",IntArr,target_callback)
    breaksub = rospy.Subscriber("/breakServo",Bool,break_callback)
    rospy.init_node("dummy_rightteensy",anonymous=False)
    rospy.loginfo("> succesfully initialised")
    while running:
        if(not breakstate):
            if dcycles>0:
                dcycles-=1
                noise = np.random.randint(-50,50)
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