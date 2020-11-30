import pygame as pg
import numpy as np
import rospy
from bot_coordinates.msg import Coordinates
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan
# from bot_coordinates.msg import Coordinates


class rob():
    def __init__(self, startX, startY, startAngle, mapp, font):
        width, height = mapp.get_size()
        self.height = height
        self.width = width
        self.radius = int(290.0*height/2000.0)
        self.surface = mapp
        self.x = startX
        self.rx = self.x
        self.font = font
        self.y = startY
        self.ry = self.y
        self.pause = True
        self.valuearray = []
        self.lidar_min_angle = 1
        self.lidar_max_angle = 1
        self.lidar_inc = 1
        self.angle = startAngle
        self.lidar = rospy.Subscriber("/lidarout", LaserScan, self.lidar_callback)
        self.mysub = rospy.Subscriber("/coords", Coordinates, self.coord_callback)
        self.breaker = rospy.Subscriber("/breakServo", Bool, self.break_callback)

    def lidar_callback(self, msg):
        self.valuearray = np.array(msg.ranges)
        self.lidar_max_angle = msg.angle_max
        self.lidar_min_angle = msg.angle_min
        self.lidar_inc = msg.angle_increment

    def coord_callback(self, msg):
        self.rx = msg.x
        self.ry = msg.y
        self.x = msg.x*self.width/3000.0
        self.y = msg.y*self.height/2000.0
        self.angle = msg.theta

    def break_callback(self, msg):
        self.pause = msg.data

    # def draw_points(self):
    #     for point in self.datapos:
    #         if point[0] != float('inf') and point[1] != float('inf'):
    #             pg.draw.circle(self.surface, (155, 0, 155), (int(point[0]), int(point[1])), 2)

    def draw_the_rays(self):
        for i in range(self.lidar_min_angle, self.lidar_max_angle, self.lidar_inc):
            angle = self.angle + i * np.pi * 2 / self.lidar_max_angle
            x2 = ((np.cos(angle)*self.valuearray[i])*self.width/3000.0)+self.x
            y2 = ((np.sin(angle)*self.valuearray[i])*self.height/2000.0)+self.y
            pg.draw.line(self.surface, (150, 150, 150), (int(self.x), int(self.y)), (int(x2), int(y2)))

    def draw(self, targetcoord):
        diff = targetcoord - np.array([self.rx, self.ry])
        e = np.linalg.norm(diff)
        colorc = (72, 5, 128)
        if self.pause:
            colorc = (22, 0, 78)
        pg.draw.circle(self.surface, colorc, (int(self.x), int(self.y)), self.radius)
        pg.draw.line(self.surface, (0, 0, 0), (int(self.x), int(self.y)), (int(self.x + self.radius*np.cos(self.angle)), int(self.y + self.radius*np.sin(self.angle))), 5)
        pg.draw.rect(self.surface, (255, 255, 255), pg.Rect(0, 0, 125, 46))
        self.font.render_to(self.surface, (0, 0), 'X: '+str(self.rx), (0, 0, 0))
        self.font.render_to(self.surface, (0, 11), 'Y: '+str(self.ry), (0, 0, 0))
        self.font.render_to(self.surface, (0, 22), 'A: '+str(self.angle), (0, 0, 0))
        self.font.render_to(self.surface, (0, 33), 'E: '+str(e), (0, 0, 0))
