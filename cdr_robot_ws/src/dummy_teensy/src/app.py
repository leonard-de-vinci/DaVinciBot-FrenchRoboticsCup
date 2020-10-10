#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr
import numpy as np #pylint ignore
import time

def target_callback(msg):
    global dtarget,dcycles
    dtarget = msg.ticks
    dcycles = msg.cycles
    rospy.loginfo("-_-_-_-_-_-_-_-_-_-_-_-_-_-")

def setup():
    global dtarget,dval,dcycles
    running = True
    dval =0
    dtarget=0
    dcycles=0
    global realitypub,targetsub
    realitypub = rospy.Publisher("/right/reality",IntArr)
    targetsub = rospy.Subscriber("right/target",IntArr,target_callback)
    rospy.init_node("dummy_teensy",anonymous=False)
    rospy.loginfo("> succesfully initialised")
    while running:
        main()
        msg = IntArr()
        msg.ticks = dval
        msg.cycles = dcycles
        realitypub.publish()
        rospy.loginfo("ticks: "+str(dval)+ " ||  cycles: "+str(dcycles))
        time.sleep(0.1)

def main():
    global dtarget,dval,dcycles
    if dcycles>0:
        dcycles-=1
        dval+=dtarget #avg +noise
        dval/=2
        dval+=np.random.randint(-5,5)


if __name__ == "__main__":
    setup()