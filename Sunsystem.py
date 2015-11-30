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

# Methode zum Erstellen von Planeten
def sphere():
    glColor3f(0.0, 0.0, 1.0)
    glutWireSphere(0.25, 30, 30)


def main():
    #  """ Game - Main """

    # Frame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5.0)

    glRotatef(0, 0, 0, 0)

    # Game-Loop
    while True:

        for event in pygame.event.get():

            # Quit-Handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotieren des Planeten
        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Um den Planeten zu drehen
        glPushMatrix()
        glRotatef(-90, 1.0, .0, .0)
        sphere()
        glPopMatrix()

        # Frame update
        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()
    quit()


main()
