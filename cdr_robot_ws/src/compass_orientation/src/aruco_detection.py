#!/usr/bin/env python
import rospy 
import numpy as np
import cv2
import cv2.aruco as aruco
from aruco_lib import *
import time
from std_msgs.msg import Bool
import signal

cap = cv2.VideoCapture(0)

det_aruco_list = {}

def signal_handler(signal, frame):
  sys.exit(0)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	rospy.init_node("compass_orientation", anonymous=False)
	orientationPub = rospy.Publisher("/compassOrientation",Bool, queue_size=1)
	while (True):
		ret,frame = cap.read()
		det_aruco_list = detect_Aruco(frame)
		if(det_aruco_list):
			angle = calculate_code_angle(frame,det_aruco_list)
			print(angle)
			if angle > 55 and angle < 120:
				rospy.loginfo("nord")
				bmsg = Bool()
				bmsg.data = True
				orientationPub.publish(bmsg)

			elif angle > 230 and angle < 310:
				rospy.loginfo("sud")
				bmsg = Bool()
				bmsg.data = False
				orientationPub.publish(bmsg)

	cap.release()


