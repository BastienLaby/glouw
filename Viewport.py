#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Map import Map, Pyramid
from OpenGL.GL import *

WIN_WIDTH = 500
WIN_HEIGHT = 500

p = Pyramid((0, 0), 50, 10, (1.0, 0.0, 0.0))
mymap = Map(WIN_WIDTH, WIN_HEIGHT)
mymap.addPyramid(p)

def render():
    pygame.display.flip()
    for k in range(len(mymap.buffer)):
        i, j = k % WIN_WIDTH, k / WIN_WIDTH
        if mymap.buffer[k]["height"] > 0.0:
            glBegin(GL_POINTS)
            glColor3f(1.0, 0.0, 0.0)
            glVertex2f(2*i / float(WIN_WIDTH), 2*j / float(WIN_HEIGHT))
            glEnd()

pygame.init()
pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
go = True
while go:
    render()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go = False
pygame.quit()



