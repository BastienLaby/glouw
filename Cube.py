# -*- coding: utf-8 -*-

import pygame
import numpy

from math import *
from OpenGL.GL import *
from OpenGL.arrays import vbo

class Cube(object):

    def __init__(self):

        self.triangleCount = 12;
        positions = numpy.array([-0.5, -0.5, 0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, -0.5, -0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, 0.5, 0.5, -0.5, -0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, -0.5, -0.5, -0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, -0.5, -0.5, 0.5, -0.5, -0.5, -0.5, 0.5, -0.5, 0.5, 0.5], dtype="float32")
        normals = numpy.array([0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0, -1, 0, 0], dtype="float32")
        uvs = numpy.array([0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0,  1.0, 0.0,  1.0, 1.0,  0.0, 1.0,  1.0, 1.0,  0.0, 0.0, 0.0, 0.0, 1.0, 1.0,  1.0, 0.0], dtype="float32")
        indices = numpy.array([0, 1, 2, 2, 1, 3, 4, 5, 6, 6, 5, 7, 8, 9, 10, 10, 9, 11, 12, 13, 14, 14, 13, 15, 16, 17, 18, 19, 17, 20, 21, 22, 23, 24, 25, 26], dtype="int32")

        self.vao = glGenVertexArrays(1)
        vboPos = glGenBuffers(1)
        vboNorm = glGenBuffers(1)
        vboUVs = glGenBuffers(1)
        vboIdx = glGenBuffers(1)

        glBindVertexArray(self.vao)

        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, vboIdx)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, vboPos)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)
        glBufferData(GL_ARRAY_BUFFER, positions, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, vboNorm)
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, None)
        glBufferData(GL_ARRAY_BUFFER, normals, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, vboUVs)
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 0, None)
        glBufferData(GL_ARRAY_BUFFER, uvs, GL_STATIC_DRAW)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def draw(self):

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.triangleCount * 3, GL_UNSIGNED_INT, None)
        glBindVertexArray(0)