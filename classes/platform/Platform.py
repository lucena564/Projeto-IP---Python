import pygame
from os import path
from constants.BackgroundConstants import BackgroundConstants

tile_size = BackgroundConstants.TILE_SIZE


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, move_x, move_y, imagem):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(
            path.join('assets', 'background', f'{imagem}'))
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        # the plataforms are going to move left an dright
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter > 50):
            self.move_direction *= -1
            self.move_counter *= -1
