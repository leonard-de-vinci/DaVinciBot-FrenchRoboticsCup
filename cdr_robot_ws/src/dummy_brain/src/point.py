import pygame as pg
import numpy as np


class waypoint:
    def __init__(self, x, y, rad, myfont, surface, mod):
        (width, height) = surface.get_size()
        self.x = x
        self.y = y
        self.rx = x*3000.00/width
        self.ry = y*2000.00/height
        self.rad = rad
        self.w = width
        self.surface = surface
        self.myfont = myfont
        self.mod = mod

    def coord(self):
        return np.array([self.x, self.y])

    def dist(self):
        return int(self.rad*self.w/3000.00)

    def draw(self, n):
        colorc = (16, 5, 135)
        if(self.mod == 1):
            colorc = (6, 186, 27)
        if(self.mod == 2):
            colorc = (240, 34, 44)
        if(self.mod == 3):
            colorc = (189, 15, 140)
        pg.draw.circle(self.surface, colorc, (int(self.x), int(self.y)), self.dist())
        self.myfont.render_to(self.surface, (int(self.x-5), int(self.y-5)), str(n), (255, 255, 255))
        self.myfont.render_to(self.surface, (int(self.x-4), int(self.y+7)), str(self.mod), (255, 255, 255))
