import pygame as pg
import numpy as np
import rospy
from bot_coordinates.msg import Coordinates

class rob():
    def __init__(self,startX,startY,startAngle,mapp):
        width,height = mapp.get_size()
        self.radius = int(290*height/2000)
        self.surface = mapp
        self.x = startX
        self.y =startY
        self.angle = startAngle
        self.mysub = rospy.Subscriber("/coords",Coordinates,self.coord_callback)
        rospy.init_node("thisvisurobot")

    def coord_callback(self,msg):
        self.x = msg.x
        self.y = msg.y
        self.angle = msg.theta 

    def draw(self):
        pg.draw.circle(self.surface,(72, 5, 128),(int(self.x),int(self.y)),self.radius)
        pg.draw.line(self.surface,(0,0,0),(int(self.x),int(self.y)),(int(self.x + self.radius*np.cos(self.angle)),int(self.y+ self.radius*np.sin(self.angle))),5)
