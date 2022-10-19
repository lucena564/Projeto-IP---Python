import pygame
from constants.BackgroundConstants import BackgroundConstants
from os import path

tile_size = BackgroundConstants.TILE_SIZE

class Exit(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(path.join('assets','background','exit.png'))
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0  