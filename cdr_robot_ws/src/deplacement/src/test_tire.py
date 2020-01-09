#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int16


class Robot():
   def __init__(self):
      rospy.init_node("test")
      rospy.loginfo("Press CTRL + C to terminate")
      self.pub = rospy.Publisher('/speedLeft', Int16, queue_size=10)
      self.pub2 = rospy.Publisher('/speedRight', Int16, queue_size=10)
      self.go = 1
      self.tirette = rospy.Subscriber ("/PinGo", Int16, self.tirette_callback)
      self.pub.publish(0)       
      self.pub2.publish(0)


      self.rate = rospy.Rate(10)
      try:
         self.run()
      except rospy.ROSInterruptException:
         pass
      finally:
         rospy.loginfo("Action finie")




   def tirette_callback(self, msg):
	self.go = msg.data
   

   def run(self):
	while (self.go == 1):
	   rospy.loginfo("J'att")
	   self.pub.publish(0)       
           self.pub2.publish(0)

        begin = rospy.get_rostime()
	rospy.loginfo("Current Time is %i %i",begin.secs,begin.nsecs)
	now = rospy.get_rostime()
	self.pub.publish(10)
	self.pub2.publish(10)   
	while (now.secs - begin.secs < 2.5):
           self.pub.publish(50)	   
           self.pub2.publish(50)
           now = rospy.get_rostime() 
	
	self.pub.publish(0)       
        self.pub2.publish(0)
	
	rospy.spin()
	   	

if __name__ == '__main__':
    try:
        whatever = Robot()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action termine.")
