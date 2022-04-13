import pygame
from settings import *
from border import Tile
from fish import *
from food import *


class display:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = yuhGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.food = Food

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'g':
                    Fish((x, y), [self.visible_sprites])
                elif col == 'y':
                    Food((x, y), [self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.visible_sprites.fish_update(self.food)


class yuhGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def fish_update(self, food):
        fish_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'fish']
        for fish in fish_sprites:
            fish.fish_update(food)



