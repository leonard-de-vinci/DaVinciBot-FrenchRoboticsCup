import rospy
from PID.msg import IntArr
from std_msgs.msg import Bool
import time
import numpy as np
class teensy():

    def __init__(self,parentTopic):
        #rospy.init_node(parentTopic+"_Dummy")
        self.realityPub = rospy.Publisher("/"+parentTopic+"/reality",IntArr,queue_size=3)
        self.targetsub = rospy.Subscriber("/"+parentTopic+"/target",IntArr,self.subcallback)
        self.breaksub = rospy.Subscriber("/breakServo",Bool,self.emergencybreakcallback)
        self.P = 30
        self.I = 30
        self.targetcycle=0
        self.targetticks = 0
        self.actualticks=0
        self.emergencybreak = True
        self.E = 0
        self.st=0.01

    def Mbreak(self):
        #rospy.loginfo("breaking")
        pass

    def emergencybreakcallback(self,msg):
        self.emergencybreak = msg.data

    def subcallback(self,msg):
        self.E = 0
        self.targetcycle = msg.cycles
        self.targetticks = abs(msg.ticks)


    def p(self,x):
        A=0.6093
        B = 2.794
        C = 99.69
        a = 1
        b = 30.04
        c = 390
        d = 2080
        return ((A*x*x)+(B*x)+C)/((a*x*x*x)+(b*x*x)+(c*x)+d)

    def calc(self):
        if(self.emergencybreak or self.targetcycle<=0):
            self.Mbreak()
        else:
            self.targetcycle-=1
            e = self.targetticks - self.actualticks
            PID = self.P*e
            self.E+=e
            PID+=min(self.I*self.E,2046)
            PID = min(PID,1023)
            PID = max(PID,0)
            self.actualticks =  self.p(PID)+ np.random.randint(-3,3)
            #rospy.loginfo(str(self.actualticks))
        

    def mainloop(self):
        while True:
            self.calc()
            msg = IntArr()
            msg.ticks = self.actualticks
            msg.cycles = self.targetcycle
            self.realityPub.publish(msg)
            time.sleep(self.st)

        