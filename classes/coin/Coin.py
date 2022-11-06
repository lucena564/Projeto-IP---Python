import pygame
from os import path
from constants.BackgroundConstants import BackgroundConstants

tile_size = BackgroundConstants.TILE_SIZE

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(path.join('assets','collectables','milk-icon.png'))
        self.image = pygame.transform.scale(img, (tile_size // 1.75, tile_size // 1.75))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)