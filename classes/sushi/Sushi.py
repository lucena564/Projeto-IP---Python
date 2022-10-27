import pygame
from constants.BackgroundConstants import BackgroundConstants
from os import path

tile_size = BackgroundConstants.TILE_SIZE

screen = BackgroundConstants.SCREEN

class Sushi(pygame.sprite.Sprite):
    def __init__(self,x,y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(path.join('assets','collectables','big_sushi.png'))
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0  

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter > 50):
            self.move_direction *= -1
            self.move_counter *= -1

    def draw(self):
        for tile in self.tile_list:
            if tile == 10:
                screen.blit(self.image, self.rect)
                pygame.draw.rect(screen,(255,255,255), self.rect,1)