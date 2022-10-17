import os
import pygame
from constants.BackgroundConstants import BackgroundConstants
from constants.WorldDataConstants import WorldDataConstants

from classes.player.Player import Player
from classes.world.World import World

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = BackgroundConstants.SCREEN_WIDTH
screen_height = BackgroundConstants.SCREEN_HEIGHT

screen = BackgroundConstants.SCREEN

pygame.display.set_caption('House of cats')

tile_size = WorldDataConstants.TILE_SIZE

player = Player(88,screen_height - 102)
world = World()

# load images
sun_img = pygame.image.load(os.path.join('assets', 'background', 'sun.png'))
bg_img = pygame.image.load(os.path.join('assets', 'background', 'sky.png'))
lib_img = pygame.image.load(os.path.join('assets', 'background','library2.png'))
# lib_img = pygame.transform.scale(lib_img,(1000,1000))

def draw_grid(): # Just to call the lines
    for line in range(0,20): # 20
        pygame.draw.line(screen, (255,255,255), (0,line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line*tile_size,0), (line*tile_size, screen_height))


run = True
while(run == True):
    
    clock.tick(fps)

    screen.blit(bg_img, (0,0))
    # screen.blit(lib_img, (0,0))
    screen.blit(sun_img, (100,100))

    world.draw()

    player.update()

    # draw_grid() # malha 100x100 - Alterar em title_size == 100 para = 10x10.

    # print(world.tile_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()