#!/usr/bin/env python
import rospy
import time
from PID.msg import FloatArr
from std_msgs.msg import Bool
from bot_coordinates.msg import command
from bot_coordinates.msg import move
from bot_coordinates.msg import target
from PID.msg import FloatArr
from std_msgs.msg import Int8
from std_msgs.msg import Bool
import signal
import sys
import numpy as np


def signal_handler(signal, frame):
    sys.exit(0)


def compassCallback(msg):
    rospy.loginfo(msg.data)
    north = msg.data


def commandCallback(msg):
    global thestack, me
    if msg.destination == me:
        thestack.append((msg.sender, msg.order, msg.precision))


def mainloop():
    global thestack, precision, state, actionpos, me, waiting, senderid, commandpub, waypointpub
    if state == 0:
        # turn on the mcontrol
        commsg = command()
        commsg.sender = me
        commsg.destination = "mcontrol"
        commsg.order = 1
        commsg.precision = 1  # here the precision refers to the rate buffer
        # trun on the gotogoal
        commsg = command()
        commsg.sender = me
        commsg.destination = "gotogoal"
        commsg.order = 1
        commsg.precision = 0  # here precision refers to the mod
        state += 1
    if state == 1:
        # TODO : wait for the start from the arduino
        # if len(thestack) > 0:
        #     a = thestack.pop()
        #     if a == ("start", 1, 2) or a == ("start", 1, 1):
        #         state += 1
        #         (_, __, precision) = a
        state += 1
        precision = 1
    if state == 2:
        # TODO load teh correct file according to the chosen strategie
        if precision == 1:  # laod the right file
            pass
        elif precision == 2:  # load the left file
            pass
        state += 1
    if state == 3:  # start ieration
        if actionpos >= len(waypoints):
            state += 1
        else:
            rospy.loginfo("action n "+(str)(actionpos))
            currentaction = waypoints[actionpos]
            # ## this is for debug only
            cmsg = command()
            cmsg.sender = me
            cmsg.destination = "a human"
            cmsg.order = 1
            cmsg.precision = 1
            commandpub.publish(cmsg)
            senderid = currentaction[0]
            # ##------------------- what are we waiting for
            waiting = currentaction[1]
            # ##------------------- hwo are we waiting for
            if senderid == 1:
                sender = "mcontrol"
            elif senderid == 2:
                sender = "gotogoal"
            # ##--------------------now that we kno what we are waiting for we check if its teh case
            skip = False
            if len(thestack) > 0:  # obtain latest msg
                (sender, order, precision) = thestack.pop()
                if sender == senderid and waiting == order:
                    actionpos += 1
                    skip = True
            if not skip:  # we need to stimulate a response
                if sender == "gotogoal":
                    msg = target()
                    msg.x = currentaction[2]
                    msg.y = currentaction[3]
                    msg.theta = currentaction[4]
                    msg.epsilon = currentaction[5]
                    waypointpub.publish(msg)
                    cmsg = command()
                    cmsg.sender = me
                    cmsg.destination = sender
                    cmsg.order = currentaction[6]
                    cmsg.precision = currentaction[7]
                    commandpub.publish(cmsg)
                    rospy.loginfo("published a waypoint")
                elif sender == "start":
                    # TODO implement the control of the servos and shit
                    pass
    if state >= 4:  # go back home because end
        //currentaction = waypoints[len(waypoints)-1]  # this line needs the last value of the waypoints to be the coord of home
        if north:
            # coordinates of north
            currentaction = [0, 0, 0, 0, 0, 50]
        else:
            # coordinates of south
            currentaction = [0, 0, 0, 0, 0, 50]
        msg = FloatArr()
        msg.x = currentaction[2]
        msg.y = currentaction[3]
        msg.theta = currentaction[4]
        msg.epsilon = currentaction[5]
        waypointpub.publish(msg)
        rospy.loginfo("go back home quick")


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    # ##---------------------waypoints and stuff
    global waypoints
    waypoints = np.array([[2, 1, 1, 1, 1, 1, 1, 1],
                          [2, 1, 1, 1, 1, 1, 1, 1],
                          [2, 1, 1, 1, 1, 1, 1, 1],
                          [2, 1, 1, 1, 1, 1, 1, 1]])
    # ##---------------------logique
    global blocked, waiting, sender, me, precision, order, state, actionpos, thestack
    blocked = False
    thestack = []
    actionpos = 0
    waiting = 0  # what we waiting for
    sender = "null"  # from whom are we waiting a message
    me = "brain"
    precision = 0
    order = 0
    state = 0

    # ##---------------------ROS
    global emergencystop, commandpub, commandsub, waypointpub, guisub, nordsub, north
    north = False
    rospy.init_node("thebrain", anonymous=False)
    nordsub = rospy.Subscriber("/compassOrientation",Bool, compassCallback)  # sub for compass
    emergencystop = rospy.Publisher("/breakServo", Bool, queue_size=1)       # pub for emergency break
    commandpub = rospy.Publisher("/control", command, queue_size=1)          # pub for commanding teh nodes
    commandsub = rospy.Subscriber("/control", command, commandCallback)      # sub for teh commands
    waypointpub = rospy.Publisher("/target", target, queue_size=1)           # pub for teh waypoints from actions
    rospy.loginfo(">  the brain has been succesfully initialised")
    while True:
        mainloop()
        time.sleep(1)
