#!/usr/bin/python
import dumdum
import sys 
import signal
import rospy

def signal_handler(signal, frame):
  sys.exit(0)

rospy.init_node("dualdummys")
r= dumdum.teensy("N2")

signal.signal(signal.SIGINT, signal_handler)

r.mainloop()