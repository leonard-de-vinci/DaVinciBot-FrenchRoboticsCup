#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float64
from std_msgs.msg import Int16
import RPi.GPIO as GPIO
import time


tire = 1

def tirette_callback(msg):
    global tire
    tire = msg.data
    #rospy.loginfo("Tirette %i", data)
    
def angle_to_percent(angle):
    start = 4
    end = 12.5
    ratio =(end-start)/180
    angle_as_percent = angle * ratio
    return start + angle_as_percent
    
def servo():
    rospy.init_node("Servo")
    rospy.loginfo("Press CTRL + C to terminate")
    tirette = rospy.Subscriber ("/PinGo", Int16, tirette_callback)
    rate = rospy.Rate(10)
    
    while(tire == 1):
        rospy.loginfo(tire)
        
        
    begin = rospy.get_time()
    now = rospy.get_time()
    while(now - begin < 95):
        now = rospy.get_time()
        rospy.loginfo("J'attends encore")
   
    servoPIN = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPIN, GPIO.OUT)
    p = GPIO.PWM(servoPIN, 50) # GPIO 23 for PWM with 50Hz
    p.start(angle_to_percent(0)) # Initialization
    time.sleep(1)

#Go at 90°
    p.ChangeDutyCycle(angle_to_percent(45))
    time.sleep(1)
   # p.ChangeDutyCycle(angle_to_percent(0))
   # time.sleep(1)
#Finish at 180°
   # p.ChangeDutyCycle(angle_to_percent(180))
   # time.sleep(1)
   # rospy.loginfo("Servo pendant encore n")
    
        
    p.stop()
    GPIO.cleanup()
    rospy.loginfo("Drapo debout !")

if __name__ == '__main__':
    try:
        servo()
    except rospy.ROSInterruptException:
        pass





    
