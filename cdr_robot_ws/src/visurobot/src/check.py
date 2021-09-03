#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Bool
from PID.msg import IntArr
from bot_coordinates.msg import Coordinates
from message_filters import ApproximateTimeSynchronizer
from message_filters import Subscriber
import numpy as np
import sys
import signal
import time

def signal_handler(signal, frame):
  rospy.signal_shutdown("manual stop")#gracefully shutdown
  sys.exit(0)

def w(angle):
    alpha = np.arctan2(np.sin(angle), np.cos(angle))
    alpha = ((np.pi + alpha) % 2*np.pi) - np.pi
    return alpha

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    X =1000.0#mm
    Y =1500.0#mm
    theta =0.0 #? rad not sure 
    rospy.init_node("rospy_tracker",anonymous=False)
    coordpub = rospy.Publisher("/coords",Coordinates,queue_size=1)
    rospy.loginfo("> tracker succesfully initialised")
    themsg = Coordinates()
    themsg.x =X
    themsg.y = Y
    themsg.ydot = 0
    themsg.xdot =0
    themsg.thetadot =0
    while True:
        time.sleep(0.2)
        theta+=0.01
        themsg.theta = w(theta)
        coordpub.publish(themsg)
