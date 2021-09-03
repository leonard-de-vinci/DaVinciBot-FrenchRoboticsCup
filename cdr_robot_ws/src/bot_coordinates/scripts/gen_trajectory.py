#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from bot_coordinates.msg import Coordinates
from bot_coordinates.srv import TrajectoryGen, TrajectoryGenResponse
import math
import numpy as np

coord = Coordinates()

def handle_trajectory_generator(req):
    distance = np.sqrt(math.pow((req.x - coord.x), 2) + math.pow((req.y - coord.y),2)) #√( (xb - xa)² + (yb - ya)² ) distance entre les anciennes coordonnées et la target en mm
    vecX = req.x - coord.x # vecteur du chemin a parcourir pour atteindre la target
    vecY = req.y - coord.y
    theta = np.arccos(vecY/(np.sqrt(math.pow(vecX,2) + math.pow(vecY,2)))) # angle du vecteur par rapport a l'axe Y : arccos(u.v/(||u||*||v||)) en rad
    compensation = 1
    if req.x < coord.x:
        compensation = -1 # si la target est a "gauche" du point actuel l'angle doit etre négatif ou sinon faut le soustraire a 360 
    newtheta = compensation*theta
    rospy.loginfo("theta : "+str(newtheta)+" | distance : "+str(distance))
    return TrajectoryGenResponse(True)

def coordsub_callback(msg):
    global coord
    coord = msg

def trajectory_generator_server():
    rospy.init_node('trajectory_generator_server')
    s = rospy.Service('trajectory_generator', TrajectoryGen, handle_trajectory_generator)
    coordsub = rospy.Subscriber("/coords", Coordinates, coordsub_callback)
    rospy.loginfo("Ready to generate trajectory.")
    rospy.spin()

if __name__ == "__main__":
    trajectory_generator_server()