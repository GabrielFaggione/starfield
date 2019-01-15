# Sprite classes
from settings import *
from random import randint
import pygame as pg

vec = pg.math.Vector2

class Star():
    def __init__(self, surface):
        self.surface = surface
        self.x = randint(-WIDTH / 2, WIDTH/2)
        self.y = randint(-HEIGHT / 2, HEIGHT/2)
        self.z = randint(WIDTH/4, WIDTH/2)
        self.pz = self.z
        self.sx = self.x
        self.sy = self.y
        self.rate = 1
    
    def update(self):
        self.lx = self.sx
        self.ly = self.sy

        self.z -= 3
        if self.z < 1:
            self.z = randint(WIDTH/4, WIDTH/2)
            self.x = randint(-HALFWIDTH, HALFWIDTH)
            self.y = randint(-HALFHEIGHT, HALFHEIGHT)

        self.sx = (self.x / self.z) * HALFWIDTH
        self.sx = int(self.sx)
        self.sy = (self.y / self.z) * HALFHEIGHT
        self.sy = int(self.sy)

        #self.px = (self.x / self.pz) * HALFWIDTH
        #self.py = (self.y / self.pz) * HALFHEIGHT

        self.rate =  int(HALFWIDTH / self.z)      
    
    def draw(self):
        pg.draw.circle(self.surface, WHITE, (int(self.sx + HALFWIDTH) , int(self.sy + HALFHEIGHT)), self.rate, self.rate)
        #pg.draw.line(self.surface, WHITE, (self.px + int(WIDTH/2), self.py + int(HEIGHT/2)), (self.sx + int(WIDTH/2), self.sy + int(HEIGHT/2)))
