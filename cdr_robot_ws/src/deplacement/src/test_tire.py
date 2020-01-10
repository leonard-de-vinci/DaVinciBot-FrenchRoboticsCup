#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int16
from sensor_msgs.msg import Range

class Robot():
   def __init__(self):
      rospy.init_node("test")
      rospy.loginfo("Press CTRL + C to terminate")
      self.pub = rospy.Publisher('/speedLeft', Int16, queue_size=10)
      self.pub2 = rospy.Publisher('/speedRight', Int16, queue_size=10)
      self.go = 1
      
      self.tirette = rospy.Subscriber ("/PinGo", Int16, self.tirette_callback)
      self.ultrasons = rospy.Subscriber("/ultrasound", Range, self.ultrasound_cb)


      self.pub.publish(0)       
      self.pub2.publish(0)
      

      self.rate = rospy.Rate(10)
      try:
         self.run()
      except rospy.ROSInterruptException:
         pass
      finally:
         rospy.loginfo("Action finie")

   def stop (self):
      self.pub.publish(0)
      self.pub2.publish(0)

   def tirette_callback(self, msg):
	   self.go = msg.data
   
   def ultrasound_cb(self, msg):
      self.distance = msg.range
      #rospy.loginfo("La distance est %i",self.distance)
   
   def straight(self, time):
      begin = rospy.get_time()
      now = rospy.get_time()
      temps_ecoule = 0
      while (now - begin < time):
         if (self.distance < 20):
            self.stop()
            temps_ecoule = rospy.get_time() - now
            rospy.loginfo("Le temps d'attente est de %i",temps_ecoule)
            continue
         self.pub.publish(40)
         self.pub2.publish(40)
         begin += temps_ecoule
         now = rospy.get_time()
         temps_ecoule = 0
      rospy.loginfo("Fin de la ligne droite")
      self.stop()
      

   def run(self):
      while(self.go == 1):
         rospy.loginfo("J'att")
         self.stop()
      
      #self.pub.publish(10)
      #self.pub2.publish(10)
      self.straight(6)
      begin = rospy.get_rostime()
      now = rospy.get_rostime()
      temps_ecoule = 0
      while (now.secs - begin.secs < 3):
         if (self.distance < 20):
            self.stop()
            temps_ecoule = rospy.get_time() - now.secs
            rospy.loginfo("Le temps d'attente est de %i",temps_ecoule)
            continue
         self.pub.publish(40)
         self.pub2.publish(20)
         rospy.loginfo("Il est censé tourner")
         begin.secs += temps_ecoule
         now = rospy.get_rostime()
         temps_ecoule = 0
      rospy.loginfo("Fin du virage")
      self.stop()
      rospy.spin()
      
               
	   	

if __name__ == '__main__':
    try:
        whatever = Robot()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action termine.")
