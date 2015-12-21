__author__ = 'cindylehner, lukaszainzinger'

import pygame
from OpenGL.raw.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Himmelskoerper():

    def __init__(self, size, color):
        self.size = size
        self.color = color
        self.rotate = None
        self.orbitB = None

    def create(self):
        glColor3f(self.color)
        glSolidSphere(self.size, 30, 30)

    def performRotate(self):
        pass


    def performOrbit(self):
        pass

    def getTexture(self):
        pass
