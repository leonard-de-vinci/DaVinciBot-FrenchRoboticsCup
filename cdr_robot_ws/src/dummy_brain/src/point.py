import pygame as pg
import numpy as np


class waypoint:
    def __init__(self, x, y, rad, myfont, surface, mod):
        width, height  = surface.get_size()
        self.x = x
        self.y = y
        self.rx = x*3000.00/width
        self.ry = y*2000.00/height
        self.rad = rad
        self.surface = surface
        self.myfont = myfont
        self.mod = mod
    
    def coord(self):
        return np.array([self.x, self.y])

    def draw(self,n):
        colorc = (16, 5, 135)
        if(self.mod == 1):
            colorc = (6, 186, 27)
        pg.draw.circle(self.surface,colorc,(self.x,self.y),self.rad)
        self.myfont.render_to(self.surface,(self.x-5,self.y-5),str(n), (255, 255, 255))
        self.myfont.render_to(self.surface,(self.x-4,self.y+7),str(self.mod), (255, 255, 255))