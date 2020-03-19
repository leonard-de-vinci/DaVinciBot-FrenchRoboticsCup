#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int16
from std_msgs.msg import Int32MultiArray

from dynamic_reconfigure.server import Server
from deplacement.cfg import RobotConfig

class Robot():
    def __init__(self):
        rospy.init_node('Control')
        rospy.loginfo('Press CTRL + C to terminate')
        self.leftSpeed = rospy.Publisher("/speedLeft", Int16, queue_size=10)
        self.rightSpeed = rospy.Publisher("/speedRight", Int16, queue_size=10)
        self.go = 1
        self.MAX_DISTANCE = 40
        self.isSafe = True
        self.distances = []
        self.ultrasoundsState = []
        self.tirette = rospy.Subscriber ("/PinGo", Int16, self.tirette_callback)
        self.ultrasons = rospy.Subscriber("/ultrasound", Int32MultiArray, self.ultrasound_cb)

        self.leftSpeed.publish(0)       
        self.rightSpeed.publish(0)
        rospy.loginfo("wheels' speed reset to 0")

        self.rate = rospy.Rate(10)
        rospy.loginfo('Control node initialized')

    def stop (self):
        self.leftSpeed.publish(0)
        self.rightSpeed.publish(0)
        rospy.loginfo("stopping wheels")


    def tirette_callback(self, msg):
        self.go = msg.data

    def ultrasound_cb(self, msg):
        temp = True
        self.ultrasoundsState = [None] * msg.layout.dim[0].size
        for i in range(msg.layout.dim[0].size):
            if (msg.data[i] > self.MAX_DISTANCE):
                self.ultrasoundsState[i] = True
            else:
                self.ultrasoundsState[i] = False
                temp = False
        self.isSafe = temp
        rospy.loginfo(self.isSafe)
        self.distances = msg.data

    def straight(self, speed, duration):
        rospy.loginfo('Starting straight line for {0} seconds at {1} speed unit'.format(duration, speed))
        begin = rospy.get_time()
        now = begin
        temps_ecoule = 0
        while (now - begin < duration):
            if rospy.is_shutdown():
                rospy.logwarn("Shutting down the node...")
                break
            if (not self.isSafe):
                self.stop()
                temps_ecoule = rospy.get_time() - now
                rospy.loginfo("Current waiting duration : %i", temps_ecoule)
                continue
            self.leftSpeed.publish(speed)
            self.rightSpeed.publish(speed)
            begin += temps_ecoule
            now = rospy.get_time()
            temps_ecoule = 0
        rospy.loginfo('End of straight line')
        self.stop()

    def turn(self, speed, duration, rotation):
        rospy.loginfo('Starting to turn {0}clockwise for {1} seconds at {2} speed unit'.format("counter " if rotation==1 else "", duration, speed))
        begin = rospy.get_rostime()
        now = begin
        temps_ecoule = 0
        while (now.secs - begin.secs < 5):
            if rospy.is_shutdown():
                rospy.logwarn("Shutting down the node...")
                break
            if (not self.isSafe):
                self.stop()
                temps_ecoule = rospy.get_time() - now.secs
                rospy.loginfo("Current waiting duration %i", temps_ecoule)
                continue

            if (rotation == 1):                         # counter clockwise
                self.leftSpeed.publish(-speed)
                self.rightSpeed.publish(-speed/2)
            elif (rotation == 0):                       # clockwise
                self.leftSpeed.publish(-speed/2)
                self.rightSpeed.publish(-speed)

            begin.secs += temps_ecoule
            now = rospy.get_rostime()
            temps_ecoule = 0
        rospy.loginfo("End of turn")
        self.stop()
    
    def spin(self, speed, duration, rotation):
        rospy.loginfo('Starting to turn {0}clockwise for {1} seconds'.format("counter " if rotation==1 else "", duration))
        begin = rospy.get_rostime()
        now = begin
        temps_ecoule = 0
        while (now.secs - begin.secs < duration):
            if rospy.is_shutdown():
                rospy.logwarn("Shutting down the node...")
                break
            if (not self.isSafe):
                self.stop()
                temps_ecoule = rospy.get_time() - now.secs
                rospy.loginfo("Current waiting duration : %i",temps_ecoule)
                continue
            
            if (rotation == 1):                         # counter clockwise
                self.leftSpeed.publish(-speed)
                self.rightSpeed.publish(0)
            elif (rotation == 0):                       # clockwise
                self.leftSpeed.publish(speed)
                self.rightSpeed.publish(0)

            begin.secs += temps_ecoule
            now = rospy.get_rostime()
            temps_ecoule = 0
        rospy.loginfo("End of spin")
        self.stop()

    def run(self, action):
        while(self.go == 1):
            rospy.loginfo("Waiting...")
            self.stop()
        
        if (action == 'straight'):
            self.straight(srv.config.direction * srv.config.speed, srv.config.duration)
        elif (action == 'turn'):
            self.turn(srv.config.direction * srv.config.speed, srv.config.duration, srv.config.rotation)
        elif (action =='spin'):
            self.spin(srv.config.direction * srv.config.speed, srv.config.duration, srv.config.rotation)

        rospy.spin()

def srvCallback(config, level):
    return config

if __name__ == '__main__':
    try:
        robot = Robot()
        srv = Server(RobotConfig, srvCallback)
        robot.MAX_DISTANCE = srv.config.max_distance
        while True:
            if (srv.config.launch):
                srv.config.launch = False
                robot.run(srv.config.action)
            robot.rate.sleep()
            if rospy.is_shutdown():
                rospy.logwarn("Shutting down the node...")
                break
    except rospy.ROSInterruptException:
        rospy.logwarn('ROS interruption detected. Exiting...')
