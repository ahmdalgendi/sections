import random
from OpenGL.GL import *
import pygame
import math
import time
def rotate(l, n):
    return l[n:] + l[:n]

class Texture:
    def __init__(self, img_name, x, y, w):
        self.img_name = img_name
        self.x = x
        self.y = y
        self.w = w
        self.Tx = 0
        self.Ty = 0
        self.rot_val = 0
        self.cube = [ (0, 0), (1, 0), (1, 1),(0, 1)]
        self.RD = 0
        self.LD = 0
        self.RU = 0
        self.LU = 0
        self.color=(1,1,1)

        self.sprite_text_id = glGenTextures(1)
        self.sprite = pygame.image.load(self.img_name)
        self.sprite_width = self.sprite.get_width()
        self.sprite_height = self.sprite.get_height()
        self.h = self.w * (self.sprite_height /self.sprite_width)
        self.sprite_data = pygame.image.tostring(self.sprite, "RGBA", 1)


        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.sprite_width, self.sprite_height, 0,
                     GL_RGBA, GL_UNSIGNED_BYTE, self.sprite_data)
        del self.sprite, self.sprite_data

    def render(self):
        a = self.x
        b = self.x + self.w
        c = self.y
        d = self.y + self.h
        self.RD = (b + self.Tx, c + self.Ty, 0)
        self.LD = (a + self.Tx, c + self.Ty, 0)
        self.RU = (b + self.Tx, d + self.Ty, 0)
        self.LU = (a + self.Tx, d + self.Ty, 0)
        glColor3f(self.color[0] ,self.color[1], self.color[2] )
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.sprite_text_id)

        glBegin(GL_QUADS)
        glTexCoord(self.cube[0][0], self.cube[0][1])
        glVertex(self.LD)

        glTexCoord(self.cube[1][0], self.cube[1][1] )
        glVertex(self.RD)

        glTexCoord(self.cube[2][0], self.cube[2][1])  # 1,1
        glVertex(self.RU)

        glTexCoord(self.cube[3][0], self.cube[3][1])
        glVertex(self.LU)
        glEnd()
        glDisable(GL_TEXTURE_2D)
    def translate(self, tx=0, ty=0):
        self.Tx = tx
        self.Ty = ty

    def rotate(self, num=1):
        self.cube = rotate(self.cube, num)
        if num % 2 == 1:
            self.h, self.w = self.w, self.h

    def color_filter(self, r=1, g=1 , b=1):
        self.color = (r, g, b)

    def scale(self, w=1 , h=1):
        self.w *=w
        self.h *=h

    def location(self):
        if self.LD  == 0 or self.RU == 0 :
            return None
        return (self.LD , self.RU)