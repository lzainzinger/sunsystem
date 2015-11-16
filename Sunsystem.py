__author__ = 'clehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """

import pygame

class Sunsystem(object):
    """  Konstruktor für das Projekt "Sunsystem"
    """
    def __init__(self):
        self.hourOfDay = 0.0
        self.dayOfYear = 0.0
        self.marsDayOfYear = 0.0