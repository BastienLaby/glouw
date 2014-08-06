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
import FPSCamera

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

def drawRepere():
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(1.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 1.0)
    glEnd()


#
# Init
#

WIN_WIDTH = 800
WIN_HEIGHT = 500

pygame.init()
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

p = Pyramid((5, 5), 5, 10, (1.0, 0.0, 0.0))
mymap = Map(MAP_WIDTH, MAP_HEIGHT)
mymap.addPyramid(p)

#
# GL Stuff
#

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
# Other stuff
#

camera = FPSCamera.FPSCamera()

#
# RenderLoop
#
fov = 25;
go = True
while go:

    # Render

    glViewport(0, 0, WIN_WIDTH, WIN_HEIGHT)

    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(shader.id)

    

    projection = Matrices.perspective(fov, WIN_WIDTH / float(WIN_HEIGHT), 1, 10000)
    view = camera.getLookatMatrix()
    glUniformMatrix4fv(projLoc, 1, GL_TRUE, projection.astype(numpy.float32))
    glUniformMatrix4fv(viewLoc, 1, GL_TRUE, view.astype(numpy.float32))
    
    # cube 1

    for i in range(10):
        for j in range(10):
            model = Matrices.translate([i * 2, 0.0, j * 2])
            glUniformMatrix4fv(modelLoc, 1, GL_TRUE, model.astype(numpy.float32))
            cube.draw()



    glUseProgram(0)
    checkGLErrors()

    pygame.display.flip()

    #
    # Events
    #

    if(pygame.key.get_pressed()[pygame.K_w]):
        camera.moveFront(0.01)
    if(pygame.key.get_pressed()[pygame.K_s]):
        camera.moveFront(-0.01)
    if(pygame.key.get_pressed()[pygame.K_a]):
        camera.moveLeft(0.01)
    if(pygame.key.get_pressed()[pygame.K_d]):
        camera.moveLeft(-0.01)

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            go = False

        elif e.type == pygame.VIDEORESIZE:
            WIN_WIDTH, WIN_HEIGHT = e.dict['size']

        elif e.type == pygame.MOUSEMOTION:      
            xrel, yrel = pygame.mouse.get_rel()
            print(xrel, yrel, ""),
            camera.rotateLeft(xrel)
            camera.rotateUp(yrel)

        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_KP1:
                fov += 1
            elif e.key == pygame.K_KP2:
                fov -= 1
            elif e.key == pygame.K_SPACE:
                camera.reset()

pygame.quit()



