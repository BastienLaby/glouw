from OpenGL.GL import *

class Texture():

    def __init__(self, internalFormat, width, height, pixelDataFormat, pixelDataType, data = None):

        self.id = glGenTextures(1)
        self.lod = 0
        glBindTexture(GL_TEXTURE_2D, self.id)
        glTexImage2D(GL_TEXTURE_2D, self.lod, internalFormat, width, height, 0, pixelDataFormat, pixelDataType, data)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glBindTexture(GL_TEXTURE_2D, 0)