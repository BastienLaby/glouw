# -*- coding: utf-8 -*-

from math import sqrt, cos

class Pyramid(object):
    
    def __init__(self, center, radius, height, color):
        self.center, self.radius, self.height, self.color = center, radius, height, color

class Map(object):
    
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.buffer = []
        for i in range(self.width * self.height):
            self.buffer.append({
                "height" : 0,
                "color" : [0, 0, 0]})

    def addPyramid(self, pyramid):
        for i in range(- pyramid.radius, pyramid.radius + 1):
            for j in range(-pyramid.radius, pyramid.radius + 1):
                distToCenter = sqrt(i**2 + j**2)
                if(distToCenter < pyramid.radius):
                    worldSpace = [i + pyramid.center[0], j + pyramid.center[1]]
                    tile = self.buffer[worldSpace[1] * self.width + worldSpace[0]]
                    tile["height"] += distToCenter / pyramid.radius




