# -*- coding: utf-8 -*-

from math import sqrt, cos

class Pyramid(object):
    
    def __init__(self, center, radius, height, color):
        self.center, self.radius, self.height, self.color = center, radius, height, color

class Map(object):
    
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.buffer = []
        for i in range(width * height):
            self.buffer.append(0)

    def addPyramid(self, pyramid):
        r = pyramid.radius
        for i in range(-r, r+1):
            for j in range(-r, r+1):
                distToPyramidCenter = abs(i) + abs(j)
                #distToPyramidCenter = sqrt(i**2 + j**2)
                if distToPyramidCenter <= pyramid.radius:
                    iWorld, jWorld = i + pyramid.center[0], j + pyramid.center[1]
                    if iWorld >= self.width or jWorld >= self.height:
                        continue
                    try:
                        print("brick in %d %d (elt %d)" % (iWorld, jWorld, jWorld * self.width + iWorld))
                        self.buffer[jWorld * self.width + iWorld] += 1
                        
                    except IndexError:
                        print("elt %d out of range" % (jWorld * self.width + iWorld))
                        pass
