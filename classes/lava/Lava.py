import pygame
from os import path
from constants.WorldDataConstants import WorldDataConstants

tile_size = WorldDataConstants.TILE_SIZE

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(path.join('assets','background','lava.png'))
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0 