#!/usr/bin/env python
import rospy
import time
from PID.msg import IntArr
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
    global instructionpub, epsilon, mod, target, buffer, feedbackpub, newtarget, bufferangle, resultant
    buffer += 1
    if buffer >= 10:  # !  so that we don't overscreen
        pos = np.array([msg.x, msg.y])
        diff = (target - pos)  # vecteur de deplacement
        diff += resultant
        distance = np.linalg.norm(diff)
        theta = np.arctan2(diff[1], diff[0])  # angle of the trajectory vector,  might need to swap argument order
        V = 0.00  # default values
        mtype = 0  # default values
        if (mod == 0):  # max speed with slow down
            V = min(((distance-epsilon)/5)+10, 40)
            mtype = 0
        elif (mod == 1):  # slow controled approch
            V = 15.00
            mtype = 0
        elif (mod == 2):  # pure rotation
            V = 20.00
            mtype = 1  # rot
        elif (mod == 3):  # rot then change behaviour for 1
            V = 20.00
            mtype = 1
        if (mod == 0 or mod == 1):  # we consider disatnce to objectif
            if (distance <= epsilon) and newtarget:  # if reached the goal
                if mod == 1:
                    V = 0.00
                theta = msg.theta  # send feedback
                tmsg = Int32()
                tmsg.data = 1
                feedbackpub.publish(tmsg)
                newtarget = False
                rospy.loginfo("reached a goal")
        if mod == 2 or mod == 3:  # we consider the angle to objectif
            if abs(w(w(theta) - w(msg.theta))) <= (0.1) and newtarget:  # if reached acceptaeble angle
                bufferangle += 1
        rospy.loginfo("----------------------"+str(bufferangle))
                if bufferangle >= 10:  # ! this value is arbitrary and might require tweeking
                    bufferangle = 0
                    if mod == 3:
                        mod = 1
    		mtype = 0
                        epsilon = 40  # ! this might need changing as in reducing for more acuracy
                        rospy.loginfo("angle held, changing behaviour")
                    else:
                        theta = msg.theta  # send feedback
                        tmsg = Int32()
                        tmsg.data = 1
                        feedbackpub.publish(tmsg)
                        newtarget = False
                        rospy.loginfo("angle held")
        controlmsg = FloatArr()
        controlmsg.v = V
        controlmsg.theta = theta
        controlmsg.type = mtype
        instructionpub.publish(controlmsg)
        # rospy.loginfo(str(theta)+" "+str(V))
        buffer = 0  # !reset limiter


def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    # alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha

def resultcallback(msg):
    global resultant
    resultant[0] = msg.x
    resultant[1] = msg.y


def movementcallback(msg):
    global target, mod, epsilon, newtarget, bufferangle
    if msg.x != target[0] or target[1] != msg.y:
        newtarget = True
        target = np.array([msg.x, msg.y])
        mod = msg.mod
        epsilon = msg.epsilon
        bufferangle = 0  # reset the buffer
        rospy.loginfo("received movement command, "+str(msg.mod))


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    # pointlist = np.loadtxt("waypoints.csv",delimiter=';')
    global coordsub, instructionpub, movementsub, feedbackpub, mod, epsilon, target, buffer, newtarget, bufferangle, resultant
    buffer = 0
    resultant = np.array([0.0, 0.0])
    bufferangle = 0  # buffer used for stability of angle
    newtarget = False
    target = np.array([1500.00, 1000.00])
    mod = 0
    epsilon = 100
    rospy.init_node("goToGoal", anonymous=False)
    instructionpub = rospy.Publisher("/control", FloatArr, queue_size=1)
    feedbackpub = rospy.Publisher("/feedback", Int32, queue_size=1)
    movementsub = rospy.Subscriber("/movement", movement, movementcallback)
    resultsub = rospy.Subscriber("/resultant_lidar", Coordinates, resultcallback)
    coordsub = rospy.Subscriber("/coords", Coordinates, coordcallback)
    rospy.loginfo("> viewer correctly initialised")
    rospy.spin()
