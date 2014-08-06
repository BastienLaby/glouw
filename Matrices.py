# -*- coding: utf-8 -*-
import math
import numpy
import transformations as tf

def perspective(fov, aspect, near, far):
    rad = fov * 2 * math.pi / 360.0
    tanHalfFovy = math.tan(rad / 2.0)
    return numpy.array([[1 / (aspect * tanHalfFovy),    0,                  0,                                0],
                       [0,                              1 / tanHalfFovy,    0,                                0],
                       [0,                              0,                  - (far + near) / (far - near),    - 2 * far * near / (far - near)],
                       [0,                              0,                  -1,                               0]])

def normalize(L):
    norm = math.sqrt(sum(a**2 for a in L))
    return [L[0] / norm, L[1] / norm, L[2] / norm]

def cross(U, V):
    return [U[1] * V[2] - U[2]*  V[1],
            U[2] * V[0] - U[0] * V[2],
            U[0] * V[1] - U[1] * V[0]]

def dot(U, V):
    return U[0] * V[0] + U[1] * V[1] + U[2] * V[2]

def rotateVector(V, axis, angle):
    angle = angle * 2 * math.pi / 360.0
    rotMat = tf.rotation_matrix(angle, axis)
    rotVec = numpy.dot(rotMat, numpy.array([V[0], V[1], V[2], 0.0]))
    return [rotVec[0], rotVec[1], rotVec[2]]

def lookat(eye, center, up):
    f = normalize([center[0] - eye[0], center[1] - eye[1], center[2] - eye[2]])
    s = normalize(cross(f, up))
    u = normalize(cross(s, f))
    return numpy.array([[s[0],   u[0],    -f[0],  -dot(s, eye)],
                        [s[1],   u[1],    -f[1],  -dot(u, eye)],
                        [s[2],   u[2],    -f[2],  dot(f, eye)],
                        [   0,      0,        0,      1]])

def translate(T):
    return numpy.array([[1,   0,    0,  T[0]],
                        [0,   1,    0,  T[1]],
                        [0,   0,    1,  T[2]],
                        [0,   0,    0,    1]])

def scale(S):
    return numpy.array([[S[0],  0,      0,      0],
                        [0,     S[1],   0,      0],
                        [0,     0,      S[2],   0],
                        [0,     0,      0,      1]])