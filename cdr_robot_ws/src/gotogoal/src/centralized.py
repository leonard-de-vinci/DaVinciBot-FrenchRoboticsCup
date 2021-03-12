#!/usr/bin/env python
import rospy
import time
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from bot_coordinates.msg import movement
from bot_coordinates.msg import move
from bot_coordinates.msg import target
from bot_coordinates.msg import command
from sensor_msgs.msg import LaserScan
from PID.msg import FloatArr
from std_msgs.msg import Int32
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def commandCallback(msg):
    global me, state, precision
    if msg.destination == me:
        state = msg.order
        precision = msg.precision


def coordCallback(msg):
    global XY, theta, targetXY, targetTheta, epsilon, state, precision, resultXY
    global movementpub, newtarget, commandpub, me
    mvmsg = move()
    theta = msg.theta
    XY = np.array([msg.x, msg.y])
    if state == 1:  # # move as intended
        diff = resultXY - XY  # ! change target to result when lidar stuff implemented
        targetangle = np.arctan2(diff[1], diff[0])
        distance = np.linalg.norm(diff)
        if precision == -1:  # freinage intelligent lidar
            mymsg = move()
            mymsg.V = 0
            mymsg.angle = theta
            mymsg.K = 0
            mymsg.A = 0
            movementpub.publish(mymsg)
            commsg = command()
            commsg.sender = me
            commsg.destination = "brain"
            commsg.order = 1  # ## successfully completed task
            commsg.precision = 1
            commandpub.publish(commsg)
        if precision == 0 or precision == 1:
            if (distance <= epsilon) and newtarget:
                newtarget = False
                commsg = command()
                commsg.sender = me
                commsg.destination = "mcontrol"
                commsg.order = 1  # ## successfully completed task
                commsg.precision = 1
                rospy.loginfo("succesfully reached destination")
                commandpub.publish(commsg)
            else:
                if precision == 0:
                    mvmsg.V = min(distance/100, 30)
                    mvmsg.K = min(1.0-(distance/3000.0), 0.6)
                    mvmsg.A = 1.0
                    mvmsg.angle = targetangle
                    movementpub.publish(mvmsg)
                if precision == 1:
                    mvmsg.V = 15
                    mvmsg.K = min(1.0-(distance/3000.0), 0.6)
                    mvmsg.A = 1.0
                    mvmsg.angle = targetangle
                    movementpub.publish(mvmsg)
                commsg = command()
                commsg.sender = me
                commsg.destination = "mcontrol"
                commsg.order = 1  # ## successfully completed task
                commsg.precision = 1
                commandpub.publish(commsg)
        elif precision == 2 or precision == 3:
            if abs(targetangle - theta) <= 0.1 and newtarget:
                if precision == 2:
                    newtarget = False
                    commsg = command()
                    commsg.sender = me
                    commsg.destination = "brain"
                    commsg.order = 1  # ## successfully completed task
                    commsg.precision = 1
                    commandpub.publish(commsg)
                    rospy.loginfo("successfully steared angle")
                elif precision == 3:
                    precision = 1
                    epsilon = 40
            else:
                if precision == 2:
                    mvmsg.V = 20
                    mvmsg.K = 0.65
                    mvmsg.A = 0
                    mvmsg.angle = targetangle
                    movementpub.publish(mvmsg)
                elif precision == 3:
                    mvmsg.V = 25
                    mvmsg.K = 0.55
                    mvmsg.A = 0
                    mvmsg.angle = targetangle
                    movementpub.publish(mvmsg)
                commsg = command()
                commsg.sender = me
                commsg.destination = "mcontrol"
                commsg.order = 1  # ## successfully completed task
                commsg.precision = 1
                commandpub.publish(commsg)
    elif state == 0:  # ## smart break
        mymsg = move()
        mymsg.V = 0
        mymsg.angle = theta
        mymsg.K = 0
        mymsg.A = 0
        movementpub.publish(mymsg)


def targetCallback(msg):
    global targetXY, targetTheta, epsilon, newtarget, commandpub, precision, state
    if msg.x != targetXY[0] or msg.y != targetXY[1]:
        newtarget = True
        targetXY = np.array([msg.x, msg.y])
        targetTheta = msg.theta
        epsilon = msg.epsilon
        rospy.loginfo("received new target coords")
        commsg = command()
        commsg.sender = me
        commsg.destination = "brain"
        commsg.order = 0  # ## we receuved feedback
        commsg.precision = state
        commandpub.publish(commsg)


def lidarcallback(laser_scan):
    # TODO implement lidar and pathplanning here
    global resultXY
    rospy.loginfo("lidar hasn t been implemented yet")
    ranges = np.array(laser_scan.ranges)
    vectors_sum = np.array([0.0,0.0])
    mid_angle = (len(ranges)//2)*laser_scan.angle_increment
    k = 0.005 #Coefficient de poids vectoriel
    for i in range(len(ranges)) :
        angle = i*laser_scan.angle_increment - mid_angle
        vectors_sum[0] += (1/laser_scan.ranges[i]**2)*np.cos(angle) + XY[0]
        vectors_sum[1] += (1/laser_scan.ranges[i]**2)*np.sin(angle) + XY[1]
    vectors_sum *= k
    resultXY = vectors_sum
    rospy.loginfo("X =  " + str(vectors_sum[0]) + " Y =  " + str(vectors_sum[1]) + " ")



if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)

    # ##---------------------STATE
    global state, me, precision
    state = 0
    precision = 0
    me = "gotogoal"  # ##! this might require changing
    newtarget = False

    # ##---------------------Lidar
    global scan, minAngle, maxAngle, stoprange
    scan = np.array([])
    minAngle = -np.pi
    maxAngle = np.pi
    stoprange = 40  # mm    #!!! this is the part that requires tweeking
    lidarvect = np.array([0, 0])

    # ##---------------------coords
    global XY, theta, targetXY, targetTheta, epsilon, resultXY
    XY = np.array([0, 0])
    resultXY = np.array([0, 0])
    targetXY = np.array([0, 0])
    theta = 0
    targettheta = 0
    epsilon = 40

    # ##---------------------ROS
    rospy.init_node("goalToPath", anonymous=False)
    global coordsub, targetsub, commandpub, commandsub, movementpub, lidarsub, emergencypub
    coordsub = rospy.Subscriber("/coords", Coordinates, coordCallback)
    targetsub = rospy.Subscriber("/target", target, targetCallback)
    commandpub = rospy.Publisher("/control", command, queue_size=1)
    commandsub = rospy.Subscriber("/control", command, commandCallback)
    movementpub = rospy.Publisher("/movement", move, queue_size=1)
    lidarsub = rospy.Subscriber("/scan", LaserScan, lidarcallback)
    rospy.loginfo(">  center succesfully initialised")
    rospy.spin()
