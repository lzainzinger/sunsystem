from pygame.constants import *

__author__ = 'cindylehner, lukaszainzinger'

""" Sonnensystem Simulation mit Hilfe von PyGame und PyOpenGL """

import pygame
from OpenGL.raw.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image
from Button import *


# class Sunsystem(object):
# """  Klasse Sunsystem zur Darstellung eines Sonnensystemes """

# Methoden zum Erstellen von Planeten
def sphereSonne():
    """ Methode zum Erstellen der Sonne  """

    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(1.0, 50, 50)


def sphereErde():
    """ Methode zum Erstellen der Erde  """

    glColor3f(0.0, 0.0, 1.0)
    glutSolidSphere(0.35, 30, 30)


def sphereMond():
    """ Methode zum Erstellen des Monds  """

    glColor3f(6, 6, 6)
    glutSolidSphere(0.1, 30, 30)


def sphereVenus():
    """
    Methode zum Erstellen der Venus
    """

    glColor3f(0.5, 0.5, 0.2)
    glutSolidSphere(0.33, 30, 30)


def sphereMars():
    """
    Methode zum Erstellen des Mars
    """

    glColor3f(1.0, 0.0, 0.0)
    glutSolidSphere(0.25, 30, 30)


def setupLighting():
    """
    Methode zum erstellen der Beleuchtung
    """
    zeros = (0.15, 0.15, 0.15, 0.3)
    ones = (1.0, 1.0, 1.0, 0.3)
    half = (0.5, 0.5, 0.5, 0.5)

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, zeros)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, half)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)
    glLightfv(GL_LIGHT0, GL_AMBIENT, zeros)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, ones)
    glLightfv(GL_LIGHT0, GL_SPECULAR, half)
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)

    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
    glEnable(GL_TEXTURE_GEN_S)
    glEnable(GL_TEXTURE_GEN_T)

    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    glShadeModel(GL_SMOOTH)


def getImage(pic):
    """
    Methode zum Laden der Textur
    :param pic: Name des Bildes (jpg) im Ordner images
    :return: textur
    """

    dateipfad = "images/" + pic + ".jpg"

    try:
        image = Image.open(dateipfad)

        x, y = image.size

        image = image.convert("RGBA").tobytes("raw", "RGBA")
        textur = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textur)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, x, y, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return textur
    except:
        raise FileNotFoundError("Textur konnte nicht geladen werden")


def setupTexture(imgID):
    """
    Methode zum Texturieren
    :param imgID: Referenz der Textur (von der Methode getImage)
    """
    glEnable(GL_TEXTURE_2D)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

    glBindTexture(GL_TEXTURE_2D, imgID)


def main():
    """
    Main-Methode des Solarsystems, zum erstellen des Solarsystems
    """
    dayOfYear = 0.0
    hourOfDay = 0.0
    venusDayOfYear = 0.0
    marsDayOfYear = 0.0
    animateIncrement = 4.0
    #  """ Game - Main """

    # Frame
    pygame.init()
    display = (800, 600)
    screen = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Sunsystem - Lehner, Zainzinger')

    # menueEins = glutCreateMenu(menue)
    # glutAddMenuEntry('Help', 1)
    # glutAttachMenu(GLUT_LEFT_BUTTON)

    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)

    gluPerspective(60, (display[0] / display[1]), 0.5, 100.0)

    glTranslatef(0.0, -0.5, -5.0)

    glRotatef(1, 1, 1, 1)

    glMatrixMode(GL_MODELVIEW)

    # Texturen laden
    textureSun = getImage('sun')
    textureMars = getImage('mars')
    textureVenus = getImage('venus')
    textureErde = getImage('erde')
    textureMond = getImage('mond')
    textureHelp = getImage('help')

    paused = False
    texture = False
    light = False
    active = True
    looky = 0.1
    lookz = 7

    # Beschreibung
    print("Key-Commands: \n  \n + ... Schneller \n - ... Langsamer \n l ... Licht \n t ... Texture \n c ... Ansicht ändern \n ESC ... Schließen")

    # Game-Loop
    while True:

        # Event-Handling
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
                if animateIncrement > 10:
                    animateIncrement = animateIncrement - 10
            elif k[K_t]:
                if texture:
                    texture = False
                    glDisable(GL_TEXTURE_2D)
                else:
                    texture = True
                    glEnable(GL_TEXTURE_2D)
                    glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
                    glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
                    glEnable(GL_TEXTURE_GEN_S)
                    glEnable(GL_TEXTURE_GEN_T)
            elif k[K_l]:
                if light:
                    light = False
                    glDisable(GL_LIGHTING)
                    glDisable(GL_LIGHT0)
                else:
                    light = True
                    setupLighting()
            elif k[K_ESCAPE]:
                pygame.quit()
                quit()
            elif k[K_c]:
                if looky == 8:
                    looky = 0.1
                    lookz = 7
                else:
                    looky = 8
                    lookz = 0

            # if event.type == pygame.MOUSEBUTTONUP:
                # mouse = pygame.mouse.get_pos()
                # if mouse[0] >= 37 and mouse[0] <= 155 and mouse[1] >= 33 and mouse[1] <= 60:
                    # print("Key-Commands: \n  \n + ... Schneller \n - ... Langsamer \n l ... Licht \n t ... Texture \n c ... Ansicht ändern \n ESC ... Schließen")

        if not paused:
            hourOfDay += animateIncrement
            inc = animateIncrement / 24.0
            dayOfYear += inc
            hourOfDay -= (hourOfDay // 24 * 24)
            dayOfYear -= (dayOfYear // 365 * 365)
            venusDayOfYear += inc
            venusDayOfYear -= (venusDayOfYear // 225 * 225)
            marsDayOfYear += inc
            marsDayOfYear -= (marsDayOfYear // 545 * 545)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -8.0)
        glRotatef(15.0, 1.0, 0.0, 0.0)

        #Button
        # glPushMatrix()

        # gluLookAt(0, 0.001, 7,
                #  0, 0, 0,
                #  0, 0, 1)
        # b1 = Button((8, -8), (12, -8), (12, -7), (8, -7))
        # b1.draw()

        # glPopMatrix()

        # Planeten

        glPushMatrix()

        gluLookAt(0, looky, lookz,
                  0, 0, 0,
                  0, 0, 1)

        if texture:
            setupTexture(textureSun)

        # Sonne
        glPushMatrix()
        glRotatef(-90, 1.0, .0, .0)
        sphereSonne()
        glPopMatrix()

        if texture:
            setupTexture(textureVenus)

        # Venus
        glRotatef(360.0 * venusDayOfYear / 225, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(2.0, 0.0, 0.0)
        glTranslatef(1.0, 0.0, 0.0)
        glRotatef(360.0 * dayOfYear / 243.0, 0.0, 1.0, 0.0)
        sphereVenus()
        glPopMatrix()

        if texture:
            setupTexture(textureErde)

        # Erde
        glRotatef(360.0 * dayOfYear / 365.0, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(5.0, 0.0, 0.0)
        glRotatef(360.0 * hourOfDay / 24.0, 0.0, 1.0, 0.0)
        sphereErde()

        if texture:
            setupTexture(textureMond)

        # Mond
        glRotatef(360.0 * 12.0 * dayOfYear / 365.0, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(0.5, 0.0, 0.0)
        sphereMond()
        glPopMatrix()
        glPopMatrix()

        if texture:
            setupTexture(textureMars)

        # Mars
        glRotatef(360.0 * marsDayOfYear / 545, 0.0, 1.0, 0.0)
        glPushMatrix()
        glTranslatef(7.0, 0.0, 0.0)
        glRotatef(360 * dayOfYear / 24.0, 0.0, 1.0, 0.0)
        sphereMars()
        glPopMatrix()
        glPopMatrix()
        # Frame Update
        glFlush()
        pygame.time.wait(40)
        pygame.display.flip()

    pygame.quit()
    quit()


main()
