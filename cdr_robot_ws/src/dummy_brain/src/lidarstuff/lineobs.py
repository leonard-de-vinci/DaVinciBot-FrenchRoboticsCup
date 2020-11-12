import pygame as pg
import numpy as np


class line():
    def __init__(self, x1, y1, x2, y2, surface):
        self.pos = np.array([x1, y1])
        self.vect = np.array([x2-x1, y2-y1])
        self.end = np.array([x2, y2])
        self.x2 = x2
        self.y2 = y2
        self.x1 = x1
        self.y1 = y1
        self.surface = surface
        self.rad = 2
        self.eraserad = 10

    def erase(self, ms):
        diff = ms - self.pos
        distance = np.linalg.norm(diff)
        if distance <= self.eraserad:
            return True
        else:
            return False

    def draw(self):
        pg.draw.circle(self.surface, (100, 100, 100), (int(self.x1), int(self.y1)), self.rad)
        pg.draw.line(self.surface, (0, 0, 0), (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), 2)