import rospy
from PID.msg import IntArr
from PID.msg import speed
from std_msgs.msg import Bool
import time
import numpy as np
# import scipy.signal as signal


class teensy():

    def __init__(self, parentTopic):
        # rospy.init_node(parentTopic+"_Dummy")
        self.parent = parentTopic
        self.realityPub = rospy.Publisher("/"+parentTopic+"/reality", speed, queue_size=3)
        self.targetsub = rospy.Subscriber("/"+parentTopic+"/target", speed, self.subcallback)
        self.breaksub = rospy.Subscriber("/breakServo", Bool, self.emergencybreakcallback)
        self.P = 30
        self.I = 30
        self.targetcycle = 0
        self.targetticks = 0
        self.actualticks = 0
        self.sens = 1
        self.dir = True
        self.emergencybreak = True
        self.E = 0
        self.st = 0.01
        self.it = 0
        self.x0 = 0
        self.lastorder = 0
        num = [0.6093, 2.794, 99.69]
        den = [1, 30.04, 390, 2080]
        # self.tf = signal.TransferFunction(num, den,dt=0.01)

    def Mbreak(self):
        self.it += 1
        if(self.it >= 6):
            rospy.loginfo(self.parent + " breaking")
            self.it = 0
        self.actualticks = 0

    def emergencybreakcallback(self, msg):
        self.emergencybreak = msg.data

    def subcallback(self, msg):
        self.E = 0
        self.dir = msg.dir
        self.targetticks = msg.ticks

    def calculate(self, x):
        orders = [self.lastorder, x]
        self.x0 = self.actualticks
        # t,y = signal.dlsim(self.tf,orders)
        self.lastorder = x
        return y[1]

    def p(self, x):
        A = 0.6093
        B = 2.794
        C = 99.69
        a = 1
        b = 30.04
        c = 390
        d = 2080
        return ((A*x*x)+(B*x)+C)/((a*x*x*x)+(b*x*x)+(c*x)+d)

    def calc(self):
        if((self.emergencybreak) or self.targetcycle <= 0):
            self.Mbreak()
        else:
            self.targetcycle -= 1
            e = self.targetticks - self.actualticks
            PID = self.P*e
            self.E += e
            PID += min(self.I*self.E, 2046)
            PID = min(PID, 1023)
            PID = max(PID, 0)
            # self.actualticks =  int(self.calculate(PID))
            self.it += 1
            if(self.it >= 6):
                rospy.loginfo(str(self.actualticks))
                self.it = 0

    def scalc(self):
        if((self.emergencybreak) or self.targetcycle <= 0):
            self.Mbreak()
        else:
            self.targetcycle -= 1
            e = self.targetticks - self.actualticks
            self.actualticks += int(e/3) + np.random.randint(-3, 3)
            self.it += 1
            if(self.it >= 6):
                rospy.loginfo(str(self.actualticks))
                self.it = 0

    def mainloop(self):
        while True:
            self.calc()
            msg = IntArr()
            msg.ticks = self.actualticks*self.sens
            msg.cycles = self.targetcycle
            self.realityPub.publish(msg)
            time.sleep(self.st)

    def simplemainloop(self):
        while True:
            self.scalc()
            msg = speed()
            msg.ticks = self.actualticks
            msg.dir = self.dir
            self.realityPub.publish(msg)
            time.sleep(self.st)
