import pygame
from settings import *


class Fish(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.sprite_type = 'fish'
        self.image = pygame.image.load('images/0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.notice_distance = 400

        self.status = 'idle'

    def get_food_distance_direction(self, food):
        fish_vec = pygame.math.Vector2(self.rect.center)
        food_vec = pygame.math.Vector2(food.rect.center)
        distance = (food_vec - fish_vec).magnitude()

        if distance > 0:
            direction = (food_vec - fish_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return distance, direction

    def actions(self, food):
        print(self.status)
        if self.status == 'move':
            self.direction = self.get_food_distance_direction(food)[1]
        else:
            self.direction = pygame.math.Vector2()

    def get_status(self, food):
        distance = self.get_food_distance_direction(food)[0]

        if distance > self.notice_distance:
            self.status = 'move'

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.rect.x += self.direction.x * speed
        self.rect.y += self.direction.y * speed
        self.rect.center = self.rect.center

    def update(self):
        self.move(self.speed)

    def fish_update(self, food):
        self.get_status(food)
        self.actions(food)

