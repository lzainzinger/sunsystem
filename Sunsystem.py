from pygame.constants import *

__author__ = 'cindylehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """

import pygame
from OpenGL.raw.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *


# class Sunsystem(object):
# """  Klasse Sunsystem zur Darstellung eines Sonnensystemes """

# Methode zum Erstellen von Planeten
def sphereSonne():
    glColor3f(1.0, 1.0, 0.0)
    glutWireSphere(1.0, 50, 50)


def sphereErde():
    glColor3f(0.0, 0.0, 1.0)
    glutWireSphere(0.35, 30, 30)


def sphereMond():
    glColor3f(6, 6, 6)
    glutWireSphere(0.1, 30, 30)


def sphereVenus():
    glColor3f(0.5, 0.5, 0.2)
    glutWireSphere(0.33, 30, 30)

def sphereMars():
    glColor3f(1.0, 0.0, 0.0)
    glutWireSphere(0.5, 30, 30)


def main():
    dayOfYear = 0.0
    hourOfDay = 0.0
    venusDayOfYear = 0.0
    marsDayOfYear = 0.0
    animateIncrement = 4.0
    #  """ Game - Main """

    # Frame
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(60, (display[0] / display[1]), 0.5, 100.0)

    glTranslatef(0.0, -0.5, -8.0)

    glRotatef(1, 1, 1, 1)

    glMatrixMode(GL_MODELVIEW)


    paused = False

    # Game-Loop
    while True:

        for event in pygame.event.get():
            k = pygame.key.get_pressed()
            # Quit-Handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if k[K_p]:
                if paused:
                    paused = False
                else:
                    paused = True
            elif k[K_PLUS]:
                if animateIncrement < 150:
                    animateIncrement = animateIncrement + 10
            elif k[K_MINUS]:
                if animateIncrement > 40:
                    animateIncrement = animateIncrement - 10





        if not paused:
            hourOfDay += animateIncrement
            inc = animateIncrement / 24.0
            dayOfYear += inc
            hourOfDay -= (hourOfDay // 24 * 24)
            dayOfYear -= (dayOfYear // 365 * 365)
            venusDayOfYear += inc
            venusDayOfYear -= (venusDayOfYear // 225 * 225)
            marsDayOfYear += inc
            marsDayOfYear -= (marsDayOfYear // 687 * 687)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8.0)
        glRotatef(15.0, 1.0, 0.0, 0.0)

        # Sonne
        glPushMatrix()
        glRotatef(-90, 1.0, .0, .0)
        sphereSonne()
        glPopMatrix()

        # Venus
        glRotatef(360.0 * venusDayOfYear / 225, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(2.0, 0.0, 0.0)
        glTranslatef(1.0, 0.0, 0.0)
        glRotatef(360.0 * dayOfYear / 243.0, 0.0, 1.0, 0.0)
        sphereVenus()
        glPopMatrix()

        # Erde
        glRotatef(360.0 * dayOfYear / 365.0, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(5.0, 0.0, 0.0)
        glRotatef(360.0 * hourOfDay / 24.0, 0.0, 1.0, 0.0)
        sphereErde()

        # Mond
        glRotatef(360.0 * 12.0 * dayOfYear / 365.0, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(0.5, 0.0, 0.0)
        sphereMond()
        glPopMatrix()
        glPopMatrix()

        glRotatef(360.0 * marsDayOfYear / 687, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(7.0, 0.0, 0.0)
        glRotatef(360 * dayOfYear / 24.0, 0.0, 1.0, 0.0)
        sphereMars()
        glPopMatrix()

        glFlush()
        # Frame update
        pygame.time.wait(40)
        pygame.display.flip()

    pygame.quit()
    quit()


main()
