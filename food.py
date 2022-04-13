import pygame
from settings import *


class Food(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_type = 'food'
        self.image = pygame.image.load('images/1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
