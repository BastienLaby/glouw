# -*- coding: utf-8 -*-

import pygame

from Matrices import lookat, cross, rotateVector, normalize

from math import cos, sin, pi

class FPSCamera(object):

    def __init__(self):
        self.reset()

    def reset(self):
        self.phi = pi
        self.theta = 0.0
        self.speed = 0.0
        self.position = [0, 0, -10]
        self.sensibility = 1
        self.computeDirectionVectors()

    def moveLeft(self, t):
        self.position[0] += t * self.left[0]
        self.position[1] += t * self.left[1]
        self.position[2] += t * self.left[2]

    def moveFront(self, t):
        self.position[0] += t * self.front[0]
        self.position[2] += t * self.front[2]

    def moveUp(self, t):
        self.position[1] += t;

    def rotateLeft(self, degrees):
        self.phi += degrees
        self.computeDirectionVectors()

    def rotateUp(self, degrees):
        if self.theta < -90.0:
            self.theta = -90.0;
        if self.theta > 90.0:
            self.theta = 90.0
        if self.theta <= 90.0 and self.theta >= -90.0:
            self.theta += degrees
            self.theta = self.theta % 360.0
            self.computeDirectionVectors();


    def getLookatMatrix(self):
        target = [0, 0, 0]
        target[0] = self.position[0] + self.front[0]
        target[1] = self.position[1] + self.front[1]
        target[2] = self.position[2] + self.front[2]
        return lookat(self.position, target, self.up);


    def computeDirectionVectors(self):
        theta = degToRad(self.theta);
        phi = degToRad(self.phi);
        self.front = [cos(theta) * sin(phi), sin(theta), cos(theta) * cos(phi)]
        self.left = [sin(phi + pi / 2.0), 0, cos(phi + pi / 2.0)]
        self.up = cross(self.front, self.left)
        print("front(%.3f, %.3f, %.3f)\tleft(%.3f, %.3f, %.3f)\tup(%.3f, %.3f, %.3f)\ttheta %.3f\tphi %.3f"
            % (self.front[0], self.front[1], self.front[2], self.left[0], self.left[1], self.left[2], self.up[0], self.up[1], self.up[2], theta, phi))

def degToRad(degree):
    return degree * 2 * pi / 360.0