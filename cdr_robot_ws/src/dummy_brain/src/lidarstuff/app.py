import pygame as pg
import numpy as np
import sys

import robot
import lineobs
pg.init()
screen = pg.display.set_mode((400, 400))

pg.display.set_caption('avoidance test')
clock = pg.time.Clock()


def create_fonts(font_sizes_list):
    "Creates different fonts with one list"
    fonts = []
    for size in font_sizes_list:
        fonts.append(
            pg.font.SysFont("Arial", size))
    return fonts


def render(fnt, what, color, where):
    global screen
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pg.Color(color))
    screen.blit(text_to_show, where)


def display_fps():
    "Data that will be rendered and blitted in _display"
    render(fonts[0], what=str(int(clock.get_fps())), color=(0, 0, 0), where=(0, 0))


# This create different font size in one line
fonts = create_fonts([12, 16, 14, 32])

bot = robot.rob(200, 200, screen)
linelist = []
circlelist = []
templist = []
mod = 1
runing = True
temppos = [0, 0]
holding = False
while runing:
    for event in pg.event.get():
        x, y = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # left click
                if mod == 0:  # move the bot
                    bot.mv(x, y)
                if mod == 1:  # line obstacle p1
                    holding = True
                    temppos = [x, y]
            elif event.button == 3:
                if mod == 0:
                    bot.point(np.array([x, y]))
                if mod == 1:
                    ms = np.array([x, y])
                    templist = []
                    for line in linelist:
                        if not line.erase(ms):
                            templist.append(line)
                    linelist = templist
                    templist = []
        elif event.type == pg.MOUSEBUTTONUP:
            if event.button == 1:  # left click
                if mod == 1:  # line obstacle p2
                    holding = False
                    linelist.append(lineobs.line(temppos[0], temppos[1], x, y, screen))
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                mod += 1
                mod = mod % 3
                print("mod:= ", mod)
            elif event.key == pg.K_DOWN:
                mod -= 1
                mod = mod % 3
                print("mod:= ", mod)

    screen.fill((255, 255, 255))
    display_fps()
    if holding:
        color = (255, 0, 0)
        if(mod == 0):
            color = (0, 0, 255)
        pg.draw.line(screen, color, (temppos[0], temppos[1]), (x, y), 1)
    bot.lidar_the_lines(linelist)
    bot.calc_lidar_resp()
    # bot.draw_the_rays()
    bot.draw_the_resp()
    # bot.draw_points()
    bot.draw()
    bot.draw_pointer()
    for line in linelist:
        line.draw()
    pg.display.update()
    clock.tick()
