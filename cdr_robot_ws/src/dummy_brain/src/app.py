#!/usr/bin/env python3
import robot
import sys
import pygame as pg
import pygame.freetype
from point import waypoint
import rospy
import datetime
from std_msgs.msg import Bool
from std_msgs.msg import Int32
from bot_coordinates.msg import movement
import numpy as np

waypoints = []


def feedback_callback(msg):
    global waypoints
    if len(waypoints) >= 1 and not emergencybreak:
        rospy.loginfo("fullfiled a waypoint")
        bybye = waypoints.pop(0)
    sendmovement()


def sendmovement():
    global mvpub, waypoints
    if len(waypoints) >= 1:
        target = waypoints[0]
        msg = movement()
        msg.x = target.rx
        msg.y = target.ry
        msg.epsilon = target.rad
        msg.mod = target.mod
        # rospy.loginfo(str(target.rx)+" | "+str(target.ry))
        mvpub.publish(msg)

# ## ROS -------------------------------------------------------------


rospy.init_node("fake_brain")
breakpub = rospy.Publisher("/breakServo", Bool, queue_size=1)
mvpub = rospy.Publisher("/movement", movement, queue_size=1)
feedbacksub = rospy.Subscriber("/feedback", Int32, feedback_callback)
# ## end ros ---------------------------------------------------------

pg.init()
myfont = pygame.freetype.SysFont('calibri', 14)
background = pg.image.load('smol.png')
screen = pg.display.set_mode(background.get_size())
width, height = background.get_size()
running = True
clock = pg.time.Clock()
thebot = robot.rob(250, 150, 0, screen, myfont)

# ## variables related to servos
servostate = [0, 0, 0]  # what pos in the angle array so either 1 or 0 atm
servoangles = [[0, 0, 0], [256, 256, 256]]  # min angle followed by max angle for easy change and switch ...

# ## other stuff
tempcoord = np.array([0, 0])
holding = False
emergencybreak = True
showlidar = False
mod = 1
targetcoord = np.array([1000, 1500])
# ## initial setups
msg = Bool()
msg.data = emergencybreak
breakpub.publish(emergencybreak)
sendmovement()

while running:
    # Did the user click the window close button?
    x, y = pygame.mouse.get_pos()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # emergency break
                emergencybreak = not emergencybreak
                msg = Bool()
                msg.data = emergencybreak
                breakpub.publish(emergencybreak)
                sendmovement()
                print("break state: ", emergencybreak)

            # ## begin the mods
            if event.key == pg.K_UP:
                mod += 1
                mod = mod % 4
                print("mod:= ", mod)
            elif event.key == pg.K_DOWN:
                mod -= 1
                mod = mod % 4
                print("mod:= ", mod)
            # ## begin the mods

            # ##begin lidar related stuff
            if event.key == pg.K_SPACE:
                showlidar = not showlidar
                print("toggle lidar ", showlidar)
            # ##end lidar stuff

            # ## begin servos
            if event.key == pg.K_a:
                which = 1
                servostate[which] = (servostate[which]+1) % 2
                # TODO put code to send info to servos here...
                print("changing position of servo nO", which)
            if event.key == pg.K_z:
                which = 2
                servostate[which] = (servostate[which]+1) % 2
                # TODO put code to send info to servos here...
            if event.key == pg.K_e:
                which = 3
                servostate[which] = (servostate[which]+1) % 2
                # TODO put code to send info to servos here...
                print("changing position of servo nO", which)
            # ## end servos

            if event.key == pg.K_s:  # save the data to csv
                name = "saves/"+np.datetime_as_string(np.datetime64(datetime.datetime.now()))+".csv"
                temparray = []
                for i in waypoints:
                    temparray.append([i.rx, i.ry, i.rad, i.mod])
                arrtosave = np.array(temparray)
                np.savetxt(name, arrtosave, delimiter=';')
                print("--------------SAVED !!! --------------")
                print(name)

        # ##begin mouse stuff
        if event.type == pygame.MOUSEBUTTONDOWN:
            temp = np.array([x, y])
            if(event.button == 1):  # left click
                holding = True
                tempcoord = temp
            elif(event.button == 3):  # right click
                newlist = []
                for point in waypoints:
                    diff = point.coord() - temp
                    if(np.linalg.norm(diff) >= (point.dist() + 3)):
                        newlist.append(point)
                waypoints = newlist
        elif event.type == pygame.MOUSEBUTTONUP:
            temp = np.array([x, y])
            if(event.button == 1):
                holding = False
                radius = np.linalg.norm(tempcoord - temp)
                if radius <= 1:
                    radius == 1
                waypoints.append(waypoint(tempcoord[0], tempcoord[1], radius, myfont, screen, mod))

    # Fill the background with white
    screen.blit(background, (0, 0))
    if len(waypoints) >= 1:
        targetcoord = np.array([waypoints[0].rx, waypoints[0].ry])
    else:
        targetcoord = np.array([thebot.rx, thebot.ry])
    thebot.draw(targetcoord)
    #if(showlidar):
    #    thebot.draw_the_rays()
    #thebot.draw(targetcoord)
    cop = waypoints[:]
    for i in range(len(cop)):
        cop[i].draw(i)
    if(showlidar):
        thebot.draw_the_rays()
    if holding:
        temp = np.array([x, y])
        colorc = (16, 5, 135)
        if(mod == 1):
            colorc = (6, 186, 27)
        if(mod == 2):
            colorc = (240, 34, 44)
        if(mod == 3):
            colorc = (189, 15, 140)
        pg.draw.line(screen, colorc, (int(tempcoord[0]), int(tempcoord[1])), (int(x), int(y)))
        radius = np.linalg.norm(tempcoord - temp)
        myfont.render_to(screen, (int(x-5), int(y-5)), str(radius), colorc)
    pg.display.flip()
    sendmovement()
    clock.tick(30)


# Done! Time to quit.
pg.quit()
