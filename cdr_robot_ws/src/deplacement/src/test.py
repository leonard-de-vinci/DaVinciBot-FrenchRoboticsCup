
#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import time
import wiringpi

rospy.init_node("test")

rospy.sleep(2.0)
#r = rospy.Rate(10) # 10hz

rospy.spin()


