#!/usr/bin/python
import sys
import pygame as pg
import rospy
from std_msgs.msg import Bool


if __name__ == '__main__':
    emergencypub = rospy.Publisher("/breakServo",Bool,queue_size=1)
    rospy.init_node("emergency_button", anonymous=False)
    rospy.loginfo("> emergency publisher correctly initialised")
    STATUS = True
    emergencypub.publish(STATUS)
    pg.init()
    # Set up the drawing window
    clock = pg.time.Clock()
    screen = pg.display.set_mode([200, 200])
    pg.display.set_caption('emergency button')
    # Run until the user asks to quit
    running = True
    while running:
        # Did the user click the window close button?
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                STATUS= not STATUS
                rospy.loginfo("pressed !! "+(str)(STATUS))
                emergencypub.publish(STATUS)
        if(STATUS):
            screen.fill((255,0,0))
        else:
            screen.fill((0,255,0))
        # Fill the background with white
        # Flip the display
        clock.tick(30)
        pg.display.flip()

    pg.quit()
