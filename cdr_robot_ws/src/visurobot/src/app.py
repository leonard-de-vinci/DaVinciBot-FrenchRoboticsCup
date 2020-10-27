#!/usr/bin/env python
import robot
import sys
import pygame as pg
import pygame.freetype
pg.init() 
myfont = pygame.freetype.SysFont('calibri', 14)
# Set up the drawing window
background = pg.image.load('smol.png')
screen = pg.display.set_mode(background.get_size())
running = True

thebot = robot.rob(250,150,0,screen,myfont)

while running:
# Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            sys.exit()
 
    # Fill the background with white
    #screen.fill((255, 255, 255))
    screen.blit(background,(0,0))
    thebot.draw()
    # Draw a solid blue circle in the center
    # Flip the display
    pg.display.flip()
 
# Done! Time to quit.
pg.quit()