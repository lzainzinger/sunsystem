__author__ = 'clehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """
class Sunsystem(object):
    def __init__(self):
        self.hourOfDay = 0.0
        self.dayOfYear = 0.0
        self.marsDayOfYear = 0.0