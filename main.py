import pygame
from pygame.locals import *
import math

class Main():
    def __init__(self):
        self.list=[]
        for i in range(150):
            x=random.randrange(0,800)
            y=random.randrange(0,600)
            self.list.append([x,y])

class Zombie(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("zombie".png").convert()
        self.image.set_colorkey((255, 255, 255))
