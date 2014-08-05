# -*- coding: utf-8 -*-
import math
import numpy

def perspective(fov, aspect, near, far):
    f = 1.0 / math.tan(fov/2.0)
    return numpy.array([[f/(aspect*1.0),    0,        0,                                0],
                       [0,                  f,        0,                                0],
                       [0,                  0,        (far+near)/(1.0*(near-far)),    2*far*near/(1.0*(near-far))],
                       [0,                  0,        -1,                               0]])

def normalize(L):
    norm = math.sqrt(sum(a**2 for a in L))
    return [L[0] / norm, L[1] / norm, L[2] / norm]

def cross(U, V):
    return [U[1] * V[2] - U[2]*  V[1],
            U[2] * V[0] - U[0] * V[2],
            U[0] * V[1] - U[1] * V[0]]

def lookat(E, C, U):
    L = normalize([C[0] - E[0], C[1] - E[1], C[2] - E[2]])
    S = normalize(cross(L, U)) # L cross U
    Ubis = normalize(cross(S, L)) # S cross L
    return numpy.array([[S[0],   Ubis[0],    -L[0],  -E[0]],
                        [S[1],   Ubis[1],    -L[1],  -E[1]],
                        [S[2],   Ubis[2],    -L[2],  -E[2]],
                        [   0,         0,        0,      1]])

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