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

        gameExit = False

        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True


        pygame.quit()
        quit()