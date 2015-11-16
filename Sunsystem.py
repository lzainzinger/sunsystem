
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

pygame.init()
display = pygame.display.set_mode((800,600))
pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

pygame.display.update()

clock = pygame.time.Clock()
exit = False

def sphere():
    n1 = [300, 200]
    n2 = [500, 200]

    pygame.draw.line(display, (1, 1, 1), (n1), (n2))

def loop():
    #  """ Game - Loop """

    while True:

        for event in pygame.event.get():
            # Quit-Handling
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill((0, 0, 0))
        sphere()
        pygame.display.update()
        clock.tick(25)
    pygame.quit()
    quit()

loop()