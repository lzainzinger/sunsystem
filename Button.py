__author__ = 'cindylehner, lukaszainzinger'
""" Button Klasse """
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.constants import *
import pygame

class Button():

    def __init__(self, p1, p2, p3, p4):
        """
        Button
        :param p1: Punkt1
        :param p2: Punkt2
        :param p3: Punkt3
        :param p4: Punkt4
        :return:
        """
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        # self.ID = ID

    def draw(self):
        """
        Zeichnet den Button
        :return:
        """

        glBegin(GL_POLYGON)
        glTexCoord2f(self.p1[0], self.p1[1])
        glVertex2f(self.p1[0], self.p1[1])
        glTexCoord2f(self.p2[0], self.p2[1])
        glVertex2f(self.p2[0], self.p2[1])
        glTexCoord2f(self.p3[0], self.p3[1])
        glVertex2f(self.p3[0], self.p3[1])
        glTexCoord2f(self.p4[0], self.p4[1])
        glVertex2f(self.p4[0], self.p4[1])
        glEnd()