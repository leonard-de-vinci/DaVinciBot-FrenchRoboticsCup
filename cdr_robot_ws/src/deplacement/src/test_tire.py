
#!/usr/bin/env python

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

      self.rate = rospy.Rate(10)
      try:
         self.run()
      except rospy.ROSInterruptException:
         pass
      finally:
         a = 1




   def tirette_callback(self, msg):
	self.go = msg.data
   

   def run(self):
	while not (rospy.is_shutdown()):
	   while (go == 1):
		a = 1
	   
	   for i in range (0, 20):
         	pub.publish(10)	   
	   	pub2.publish(10)
	   	

if __name__ == '__main__':
    try:
        whatever = Robot()
    except rospy.ROSInterruptException:
        rospy.loginfo("Action terminée.")
