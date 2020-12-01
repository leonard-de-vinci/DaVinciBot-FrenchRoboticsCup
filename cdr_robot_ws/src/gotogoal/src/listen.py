#!/usr/bin/env python
import rospy 
import time
from bot_coordinates.msg import Coordinates
from bot_coordinates.msg import movement
from PID.msg import FloatArr
from std_msgs.msg import Int32
import signal
import sys
import numpy as np

def signal_handler(signal, frame):
  sys.exit(0)

def coordcallback(msg):
    global  instructionpub, epsilon, mod, target, buffer, feedbackpub
    buffer +=1
    if buffer >= 5: #! so that we don't overscreen
        pos =  np.array([msg.x,msg.y])
        diff  = target - pos #vecteur de deplacement
        distance = np.linalg.norm(diff)
        theta = np.arctan2(diff[1],diff[0])#angle of the trajectory vector,  might need to swap argument order
        #! taking care of the speed
        V = 20.00
        if (mod == 1):
            V = min(distance/7,V)
        if distance<=epsilon:
            if mod == 1:
                V=0.00
            theta = msg.theta
            tmsg=Int32()
            tmsg.data = 1
            feedbackpub.publish(tmsg)
        controlmsg = FloatArr()
        controlmsg.v = V
        controlmsg.theta = theta
        instructionpub.publish(controlmsg)
        rospy.loginfo(str(theta)+" "+str(V))
        buffer=0#!reset limiter

def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    #alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha

def movementcallback(msg):
    global target, mod, epsilon
    target = np.array([msg.x, msg.y])
    mod = msg.mod
    epsilon = msg.epsilon
    rospy.loginfo("received movement command")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    #pointlist = np.loadtxt("waypoints.csv",delimiter=';')
    global  coordsub, instructionpub, movementsub, feedbackpub, mod, epsilon, target, buffer
    buffer = 0
    target = np.array([1500.00,1000.00])
    mod = 0
    epsilon = 100
    rospy.init_node("goToGoal", anonymous=False)
    instructionpub = rospy.Publisher("/control", FloatArr,queue_size=1)
    feedbackpub = rospy.Publisher("/feedback", Int32,queue_size=1)
    movementsub = rospy.Subscriber("/movement", movement,movementcallback)
    coordsub = rospy.Subscriber("/coords",Coordinates,coordcallback)     
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()