from pygame.constants import DOUBLEBUF, OPENGL

__author__ = 'cindylehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """

import pygame
from OpenGL.raw.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *

# class Sunsystem(object):
# """  Klasse Sunsystem zur Darstellung eines Sonnensystemes """

    # def __init__(self):
    #    self.hourOfDay = 0.0
     #   self.dayOfYear = 0.0
      #  self.marsDayOfYear = 0.0



def sphere():
    glColor3f(1.0,1.0,1.0)
    glutSolidSphere(0.25,250,250)


def main():
    #  """ Game - Main """

    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    glRotatef(20, 0, 0, 0)

    while True:

        for event in pygame.event.get():
            # Quit-Handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # display.fill((0,0,0))
        sphere()
        pygame.display.flip()
        pygame.time.wait(10)
    pygame.quit()
    quit()

main()