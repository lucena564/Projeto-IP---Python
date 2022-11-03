import pygame
from os import path
from constants.BackgroundConstants import BackgroundConstants

screen = BackgroundConstants.SCREEN
class Enemy(pygame.sprite.Sprite): # Esse parametro é para estilo de jogo sprite (como o nosso)
    # Dentro desse método 'pygame.sprite.Sprite' já temos um método "draw" p/ aparecer o nosso inimigo.
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self) # É uma função do pygame para inimigos.
        self.image = pygame.image.load(path.join('assets','enemies','blob','little.png')) # Trocar por um cachorro
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter > 50):
            self.move_direction *= -1
            self.move_counter *= -1

    def draw(self):
        for tile in self.tile_list:
            if tile == 3:
                screen.blit(self.image, self.rect)
                pygame.draw.rect(screen,(255,255,255), self.rect,1)