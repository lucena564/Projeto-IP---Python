import os
import pygame
from constants.WorldDataConstants import WorldDataConstants
from constants.BackgroundConstants import BackgroundConstants

class World():
    def __init__(self):
        self.tile_list = []

        # Load images
        dirt_img = pygame.image.load(os.path.join('assets', 'background', 'dirt.png'))
        grass_img = pygame.image.load(os.path.join('assets', 'background','grass.png'))
        # lava_img = pygame.image.load('img/lava.png')

        row_count = 0
        for row in WorldDataConstants.MAP_DIMENSIONS:
            col_count = 0
            for tile in row:
                if tile == 1: 
                    img = pygame.transform.scale(dirt_img, (WorldDataConstants.TILE_SIZE, WorldDataConstants.TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * WorldDataConstants.TILE_SIZE
                    img_rect.y = row_count * WorldDataConstants.TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2: # Grama
                    img = pygame.transform.scale(grass_img, (WorldDataConstants.TILE_SIZE, WorldDataConstants.TILE_SIZE))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * WorldDataConstants.TILE_SIZE
                    img_rect.y = row_count * WorldDataConstants.TILE_SIZE
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            BackgroundConstants.SCREEN.blit(tile[0], tile[1])
            pygame.draw.rect(BackgroundConstants.SCREEN,(255,255,255), tile[1], 2)
