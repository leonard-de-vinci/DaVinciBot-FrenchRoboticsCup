#!/usr/bin/env python
import rospy 
import time
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from PID.msg import FloatArr
import signal
import sys
import numpy as np

def signal_handler(signal, frame):
  sys.exit(0)

def coordcallback(msg):
    global itlist,pointlist, instructionpub ,repit
    repit+=1
    if(repit>=5):
        target = pointlist[itlist%(len(pointlist))]
        pos =  np.array([msg.x,msg.y])
        diff  = target - pos #vecteur de deplacement
        distance = np.linalg.norm(diff)
        epsylon = 10
        if distance<=epsylon:
            itlist+=1
            target = pointlist[itlist%(len(pointlist))]
            diff  = target - pos #vecteur de deplacement vers prochain point
            distance = np.linalg.norm(diff)
        V = min(distance/10,48) #fonction de control de la vitesse en fonction de la distance,  will be upgraded
        theta = np.arctan2(diff[1],diff[0])#angle of the trajectory vector,  might need to swap argument order
        controlmsg = FloatArr()
        controlmsg.v = V
        controlmsg.theta = theta
        instructionpub.publish(controlmsg)
        rospy.loginfo(str(itlist))
        rospy.loginfo(str(theta)+" "+str(V))
        repit=0#!reset limiter
def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    #alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    global pointlist , itlist ,repit
    itlist = 0
    repit=0
    pointA = np.array([200,200])
    pointB = np.array([2800,1800])
    pointC = np.array([200,1800])
    pointlist = [pointA,pointB,pointC]
    global  coordsub, instructionpub
    rospy.init_node("goToGoal", anonymous=False)
    instructionpub = rospy.Publisher("/control",FloatArr,queue_size=3)
    coordsub = rospy.Subscriber("/coords",Coordinates,coordcallback) 
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()