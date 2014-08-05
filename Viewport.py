#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import math

import pygame
import numpy
from OpenGL.GL import *

from Map import Map, Pyramid
import Shader
import Cube
import Matrices
import Texture

MAP_WIDTH = 20
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


def checkGLErrors():
    if(glGetError() != GL_NO_ERROR):
        print('Error OpenGL : ' + str(glGetError()))


#
# Init data for rendering
#

WIN_WIDTH = 1280
WIN_HEIGHT = 860

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

p = Pyramid((5, 5), 5, 10, (1.0, 0.0, 0.0))
mymap = Map(MAP_WIDTH, MAP_HEIGHT)
mymap.addPyramid(p)

cube = Cube.Cube()

shader = Shader.Shader("shader.vs.glsl", "shader.fs.glsl")

projLoc = glGetUniformLocation(shader.id, "u_projection")
viewLoc = glGetUniformLocation(shader.id, "u_view")
modelLoc = glGetUniformLocation(shader.id, "u_model")

texColor = Texture.Texture(GL_RGBA8, WIN_WIDTH, WIN_HEIGHT, GL_RGBA, GL_UNSIGNED_BYTE)
texDepth = Texture.Texture(GL_DEPTH_COMPONENT24, WIN_WIDTH, WIN_HEIGHT, GL_DEPTH_COMPONENT, GL_FLOAT)

fbo = glGenFramebuffers(1)
glBindFramebuffer(GL_FRAMEBUFFER, fbo)
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texColor.id, 0)
glFramebufferTexture2D(GL_FRAMEBUFFER, GL_DEPTH_ATTACHMENT, GL_TEXTURE_2D, texDepth.id, 0)
glBindFramebuffer(GL_FRAMEBUFFER, 0)

checkGLErrors()

#
# RenderLoop
#

go = True
while go:

    # Render

    # glBindFramebuffer(GL_FRAMEBUFFER, fbo)
    # glDrawBuffer(GL_COLOR_ATTACHMENT0)

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(shader.id)

    projection = Matrices.perspective(5, WIN_WIDTH / float(WIN_HEIGHT), 0.001, 1000)
    view = Matrices.lookat((0, 0, 2), (0, 0, 0), (0, 1, 0))
    model = Matrices.translate((math.cos(time.time()), 0.0, 0.0))
    glUniformMatrix4fv(projLoc, 1, GL_TRUE, projection.astype(numpy.float32))
    glUniformMatrix4fv(viewLoc, 1, GL_TRUE, view.astype(numpy.float32))
    glUniformMatrix4fv(modelLoc, 1, GL_TRUE, model.astype(numpy.float32))

    cube.draw()
    # glBindFramebuffer(GL_FRAMEBUFFER, fbo)

    # Blit on screen

    # glBindFramebuffer(GL_READ_FRAMEBUFFER, fbo)
    # glBindFramebuffer(GL_DRAW_FRAMEBUFFER, 0)
    # glReadBuffer(GL_COLOR_ATTACHMENT0)
    # glDrawBuffer(GL_BACK)

    glUseProgram(0)

    checkGLErrors()

    pygame.display.flip()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            go = False
        elif e.type == pygame.VIDEORESIZE:
            WIN_WIDTH, WIN_HEIGHT = e.dict['size']

pygame.quit()



