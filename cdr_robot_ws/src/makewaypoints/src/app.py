#!/usr/bin/env python
import sys
import pygame as pg
import pygame.freetype
import numpy as np


pg.init() 
myfont = pygame.freetype.SysFont('calibri', 14)
# Set up the drawing window
background = pg.image.load('smol.png')
screen = pg.display.set_mode(background.get_size())
running = True
clock = pygame.time.Clock()

width,height = background.get_size()

waypoints = []
if len(sys.argv)==2:
    loadedarr = np.loadtxt(sys.argv[1], delimiter=';')
    print("editing file:",sys.argv[1])
    for i in loadedarr:
        temp = i
        temp[0] = temp[0]*width/3000
        temp[1] = temp[1]*height/2000
        waypoints.append(temp)
else:
    print(" no or invalid args were provided")


while running:
# Did the user click the window close button?
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print("exit without saving")
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RETURN:#save waypoints
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            temp = np.array([x,y])
            if(event.button==1):#left click
                waypoints.append(temp)
            else:
                newlist=[]
                for point in waypoints:
                    diff = point - temp
                    if(np.linalg.norm(diff)>=10):
                        newlist.append(point)
                waypoints = newlist                
    # Fill the background with white
    #screen.fill((255, 255, 255))
    screen.blit(background,(0,0))
    # Draw a solid blue circle in the center
    # Flip the display
    for i in range(len(waypoints)):
        point = waypoints[i]
        x = point[0]
        y = point[1]
        pg.draw.circle(screen,(16, 5, 135),(x,y),10)
        myfont.render_to(screen,(x-5,y-5),str(i), (255, 255, 255))
    pg.display.flip()
    clock.tick(30)#30fps for vm friendly
 
for i in waypoints:
    i[0] = i[0]*3000.0/width
    i[1] = i[1]*2000.0/height
nparr = np.array(waypoints)
np.savetxt('waypoints.csv', nparr, delimiter=';')
print("saved with succes to waypoints.csv")
# Done! Time to quit.
pg.quit()