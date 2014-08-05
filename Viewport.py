#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from Map import Map, Pyramid
from OpenGL.GL import *

WIN_WIDTH = 500
WIN_HEIGHT = 500

MAP_WIDTH = 10
MAP_HEIGHT = MAP_WIDTH
TILE_SCREEN_WIDTH = 1 / float(MAP_WIDTH)

def drawGrid(tilemap):
    for i in range(MAP_WIDTH + 1):
        x = (i - MAP_WIDTH / float(2.0)) / float(MAP_WIDTH * 0.5)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(x, -1)
        glVertex2f(x, 1)
        glEnd()
    for j in range(MAP_HEIGHT + 1):
        y = (j - MAP_HEIGHT / float(2.0)) / float(MAP_HEIGHT * 0.5)
        glBegin(GL_LINES)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(-1, y)
        glVertex2f(1, y)
        glEnd()

def drawTile(i, j):
    xScreen = ((i / float(MAP_WIDTH - 1)) - 0.5) * float(MAP_WIDTH - 1) / (MAP_WIDTH * 0.5)
    yScreen = - ((j / float(MAP_WIDTH - 1)) - 0.5) * float(MAP_WIDTH - 1) / (MAP_WIDTH * 0.5)
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(xScreen - TILE_SCREEN_WIDTH, yScreen + TILE_SCREEN_WIDTH)
    glVertex2f(xScreen + TILE_SCREEN_WIDTH, yScreen + TILE_SCREEN_WIDTH)
    glVertex2f(xScreen + TILE_SCREEN_WIDTH, yScreen - TILE_SCREEN_WIDTH)
    glVertex2f(xScreen - TILE_SCREEN_WIDTH, yScreen - TILE_SCREEN_WIDTH)
    glEnd()

def render(tilemap):
    
    for i in range(MAP_WIDTH * MAP_HEIGHT):
        if tilemap.buffer[i] > 0:
            ii = (i % MAP_WIDTH)
            jj = (i / MAP_WIDTH)
            drawTile(ii, jj)
    drawGrid(tilemap)
    pygame.display.flip()





p = Pyramid((5, 5), 5, 10, (1.0, 0.0, 0.0))
mymap = Map(MAP_WIDTH, MAP_HEIGHT)
mymap.addPyramid(p)

pygame.init()
pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
go = True
while go:
    render(mymap)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go = False

pygame.quit()



