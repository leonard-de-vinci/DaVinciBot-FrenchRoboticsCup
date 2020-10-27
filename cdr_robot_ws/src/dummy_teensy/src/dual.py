#!/usr/bin/python
import dumdum
import threading
import time
import sys
import signal
import rospy

rospy.init_node("dualdummys")
rightdummy = dumdum.teensy("N2")
leftdummy = dumdum.teensy("N1")
rospy.loginfo("nodes are runnning, no noise to be seen...")
global t1,t2

t1 = threading.Thread(target=rightdummy.mainloop)
t2 = threading.Thread(target=leftdummy.mainloop)

t1.start()
t2.start()

def signal_handler(signal, frame):
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
    time.sleep(2)