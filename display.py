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

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'g':
                    self.fish = Fish((x, y), [self.visible_sprites])
                elif col == 'y':
                    self.food = Food((x, y), [self.visible_sprites, self.obstacle_sprites])

    def fish_eat_logic(self):
        if self.fish:
            collision_sprites = pygame.sprite.spritecollide(self.fish, self.obstacle_sprites, True)
            if collision_sprites:
                for target_sprite in collision_sprites:
                    target_sprite.kill()

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        self.visible_sprites.fish_update(self.food)
        self.fish_eat_logic()


class yuhGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def fish_update(self, food):
        fish_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'fish']
        for fish in fish_sprites:
            fish.fish_update(food)



