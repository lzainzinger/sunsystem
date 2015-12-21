__author__ = 'lukaszainzinger'
from OpenGL.raw.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Button():

    def __init__(self, p1, p2, p3, p4, ID):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.ID = ID

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.p1[0], self.p1[1])
        glVertex2f(self.p2[0], self.p2[1])
        glVertex2f(self.p3[0], self.p3[1])
        glVertex2f(self.p4[0], self.p4[1])
        glEnd()