__author__ = 'cindylehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

class Sunsystem(object):
    """  Konstruktor für das Projekt "Sunsystem"
    """
    def __init__(self):
        self.hourOfDay = 0.0
        self.dayOfYear = 0.0
        self.marsDayOfYear = 0.0

        pygame.init()
        display = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

        pygame.display.update()

        while True:

            for event in pygame.event.get():
                # Quit-Handling
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.fill(0,0,0)
            pygame.time.Clock().tick(25)