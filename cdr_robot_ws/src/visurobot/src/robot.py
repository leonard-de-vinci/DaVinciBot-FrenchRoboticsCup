import pygame as pg
import numpy as np
import rospy
from bot_coordinates.msg import Coordinates
#from bot_coordinates.msg import Coordinates

class rob():
    def __init__(self,startX,startY,startAngle,mapp,font):
        width,height = mapp.get_size()
        self.height = height
        self.width = width
        self.radius = int(290.0*height/2000.0)
        self.surface = mapp
        self.x = startX
        self.rx =self.x
        self.font = font
        self.y =startY
        self.ry = self.y
        self.angle = startAngle
        self.mysub = rospy.Subscriber("/coords",Coordinates,self.coord_callback)
        rospy.init_node("thisvisurobot")

    def coord_callback(self,msg):
        self.rx = msg.x
        self.ry = msg.y
        self.x = msg.x*self.width/3000.0
        self.y = msg.y*self.height/2000.0
        self.angle = msg.theta 

    def draw(self):
        pg.draw.circle(self.surface,(72, 5, 128),(int(self.x),int(self.y)),self.radius)
        pg.draw.line(self.surface,(0,0,0),(int(self.x),int(self.y)),(int(self.x + self.radius*np.cos(self.angle)),int(self.y+ self.radius*np.sin(self.angle))),5)
        self.font.render_to(self.surface,(0,0),'X: '+str(self.rx), (0, 0, 0))
        self.font.render_to(self.surface,(0,11),'Y: '+str(self.ry), (0, 0, 0))
        self.font.render_to(self.surface,(0,22),'A: '+str(self.angle), (0, 0, 0))
