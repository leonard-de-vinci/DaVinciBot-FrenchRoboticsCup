import numpy as np
import pygame as pg


class rob:
    def __init__(self, x, y, surface):
        self.pos = np.array([x, y])
        self.movement = np.array([1, 1])
        self.theta = 0.0310
        self.v = 0
        self.objectif = np.array([200, 200])
        self.rad = 10
        self.N = 100
        self.minresp = 1
        self.lidarres = np.array([0.00, 0.00])
        self.maxdist = 3000
        self.securitydist = 2
        self.surface = surface
        self.datapos = np.ones((self.N, 2))
        self.datadist = np.ones((self.N, 1)) * self.maxdist
        self.dataresp = np.zeros((self.N, 1))

    def mv(self, x, y):
        self.pos = np.array([x, y])

    def point(self, ms):
        self.objectif = ms
        # diff = ms - self.pos
        # self.v = np.linalg.norm(diff)
        # self.theta = np.arctan2(diff[1], diff[0])

    def draw_pointer(self):
        pg.draw.line(self.surface, (0, 150, 0), (int(self.pos[0]), int(self.pos[1])), (int(self.objectif[0]), int(self.objectif[1])), 2)
        # x2 = self.pos[0] + np.cos(self.theta)*self.v
        # y2 = self.pos[1] + np.sin(self.theta)*self.v
        # pg.draw.line(self.surface, (0, 150, 0), (int(self.pos[0]), int(self.pos[1])), (int(x2), int(y2)), 2)
        x2 = self.pos[0] + self.lidarres[0]
        y2 = self.pos[1] + self.lidarres[1]
        pg.draw.line(self.surface, (255, 0, 0), (int(self.pos[0]), int(self.pos[1])), (int(x2), int(y2)), 2)

    def draw(self):
        pg.draw.circle(self.surface, (100, 100, 100), (int(self.pos[0]), int(self.pos[1])), self.rad)

    def calc_lidar_resp(self):
        self.lidarres = np.array([0.00, 0.00])
        for i in range(self.N):
            val = self.dataresp[i] * 30000
            if val >= self.minresp:
                angle = self.theta + i * 2 * np.pi / self.N
                x2 = np.cos(angle + np.pi)*val
                y2 = np.sin(angle + np.pi)*val
                temp = np.array([float(x2), float(y2)])
                self.lidarres += temp
        self.lidarres /= self.N

    def lidar_the_lines(self, lines):
        self.datadist = np.ones((self.N, 1)) * self.maxdist
        self.dataresp = np.zeros((self.N, 1))
        self.datapos = np.tile(self.pos, (self.N, 1))
        for line in lines:
            for i in range(self.N):
                angle = self.theta + (i * np.pi * 2 / self.N)
                x2 = np.cos(angle) * self.maxdist + self.pos[0]
                y2 = np.sin(angle) * self.maxdist + self.pos[1]
                rx, ry = get_intersect(self.pos, [x2, y2], line.pos, line.end)
                r = np.array([rx, ry])
                diff = r-self.pos
                dist = np.linalg.norm(diff) - self.securitydist - self.rad
                if dist < self.datadist[i] and dist > 0.01:
                    self.datadist[i] = dist
                    self.dataresp[i] = 1/(dist*dist)
                    self.datapos[i] = r

    def draw_the_rays(self):
        for i in range(self.N):
            angle = self.theta + i * np.pi * 2 / self.N
            x2 = (np.cos(angle)*self.datadist[i])+self.pos[0]
            y2 = (np.sin(angle)*self.datadist[i])+self.pos[1]
            pg.draw.line(self.surface, (150, 150, 150), (int(self.pos[0]), int(self.pos[1])), (int(x2), int(y2)))

    def draw_the_resp(self):
        for i in range(self.N):
            val = self.dataresp[i] * 30000
            if val >= self.minresp:
                angle = self.theta + i * 2 * np.pi / self.N
                coord = self.datapos[i]
                x2 = coord[0] + np.cos(angle + np.pi)*val/2
                y2 = coord[1] + np.sin(angle + np.pi)*val/2
                pg.draw.line(self.surface, (255, 0, 255), (int(coord[0]), int(coord[1])), (int(x2), int(y2)), 2)

    def draw_points(self):
        for point in self.datapos:
            if point[0] != float('inf') and point[1] != float('inf'):
                pg.draw.circle(self.surface, (155, 0, 155), (int(point[0]), int(point[1])), 2)

def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2, b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1, a2, b1, b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1))))  # h for homogeneous
    l1 = np.cross(h[0], h[1])            # get first line
    l2 = np.cross(h[2], h[3])            # get second line
    x, y, z = np.cross(l1, l2)           # point of intersection
    if z == 0:                           # lines are parallel 
        return (float('inf'), float('inf'))
    x = x/z
    y = y/z
    if x >= max(b1[0], b2[0]) or x <= min(b1[0], b2[0]) or y >= max(b1[1], b2[1]) or y <= min(b1[1], b2[1]):
        return (float('inf'), float('inf'))
    if x >= max(a1[0], a2[0]) or x <= min(a1[0], a2[0]) or y >= max(a1[1], a2[1]) or y <= min(a1[1], a2[1]):
        return (float('inf'), float('inf'))
    return (x, y)
