# Ler levels_data.py

from os import path
import pickle
import pygame
from pygame import mixer
from constants.BackgroundConstants import BackgroundConstants
from classes.button.Button import Button 

from classes.player.Player import Player
from classes.coin.Coin import Coin
from classes.world.World import World, blob_group, lava_group, exit_group, coin_group

from levels.levels_data import *

pygame.mixer.pre_init(44100, -16, 2, 512) # Peguei essa config na net para rodar a musica direitinho.
mixer.init()
pygame.init()

clock = pygame.time.Clock()

font_miau = pygame.font.SysFont("Bauhaus 93", 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30) # Método para definir fonte

# Cor em rgb
white = (255, 255, 255) 
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

fps = 60
game_over = 0
main_menu = True
level = 0
max_levels = 7
score = 0


screen_width = BackgroundConstants.SCREEN_WIDTH
screen_height = BackgroundConstants.SCREEN_HEIGHT

screen = BackgroundConstants.SCREEN

pygame.display.set_caption('House of cats')

tile_size = BackgroundConstants.TILE_SIZE

# Load images
# sun_img = pygame.image.load(path.join('assets', 'background', 'sun.png'))
# # bg_img = pygame.image.load(path.join('assets', 'background', 'sky_coin.jpg'))
# bg_img = pygame.image.load(path.join('assets', 'background', 'sky.png'))
# lib_img = pygame.image.load(path.join('assets', 'background','library2.png'))

restart_img = pygame.image.load(path.join('assets', 'menu','restart_btn.png'))
start_img = pygame.image.load(path.join('assets', 'menu','start_btn.png'))
exit_img = pygame.image.load(path.join('assets', 'menu', 'exit_btn.png'))

restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

# Load sounds
coin_fx = pygame.mixer.Sound(path.join('sound', 'coin.wav'))
coin_fx.set_volume(0.5)
     # jump_fx and game_over_fx is defined at Player.py
# jump_fx = pygame.mixer.Sound(path.join('sound', 'jump.wav'))
# jump_fx.set_volume(0.5)
# game_over_fx = pygame.mixer.Sound(path.join('sound', 'game_over.wav'))
# game_over_fx.set_volume(0.2)
# door_fx = pygame.mixer.Sound(path.join('sound', 'Ta-Da-meme.wav'))
# door_fx.set_volume(0.5)

# Creating a static coin for score - Had to import Coin class.
score_coin = Coin((tile_size // 2) + 50, (tile_size // 2) + 0) 
coin_group.add(score_coin)


level_ = 0
world_data = next_level_array[0][level_]
image_name = next_level_array[2][level_]
world = World(world_data, image_name)

player = Player(88,screen_height - 102)



# lib_img = pygame.transform.scale(lib_img,(1000,1000))

def draw_grid(): # Just to call the lines
    for line in range(0,20): # 20
        pygame.draw.line(screen, (255,255,255), (0,line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line*tile_size,0), (line*tile_size, screen_height))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_level(level):
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()

    # print(level)
        
    world_data = next_level_array[level][0]
<<<<<<< HEAD
    image_name = next_level_array[2][level_]
=======
    image_name = next_level_array[level][2]
>>>>>>> 07cf8b997f87794e59c19a5c844381ae30008239
    world = World(world_data, image_name)

    return world

run = True

mapa_skip = 1
# All game run here.
while(run == True):
    
    clock.tick(fps)

    # Tela base do jogo. Colocaremos algumas condições no futuro para o plano de fundo mudar com o nível.
    # screen.blit(bg_img, (0,0))
    # screen.blit(sun_img, (100,100))
    screen.blit(next_level_array[level_][1], (0,0))

    if main_menu == True:
        if exit_button.draw() == True:
            run = False

        if start_button.draw() == True:
            main_menu = False

    else:

        world.draw()
        draw_text(' X ' + str(score), font_score, black , tile_size + 40, 17)

        if game_over == 0:
            blob_group.update()

            # Update score
            # Check if a coin has been collected
            if pygame.sprite.spritecollide(player, coin_group, True): # True parameter is to colect the coin and hide it inside the map.
                coin_fx.play()
                score += 1

                # if score == 1:
                #     print(f'Moeda coletada = {score}')
                
                # else:
                #     print(f'Moedas coletadas = {score}')     

            # draw_text(' X ' + str(score), font_score, black , tile_size + 40, 17)
        
        blob_group.draw(screen)
        lava_group.draw(screen)
        coin_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over, world)

        # If player died
        if game_over == -1:
            # game_over_fx.play()
            draw_text('Miaaaaaaaau!!!', font_miau, blue, (screen_width // 2) - 140, screen_height // 2)
            if restart_button.draw() == True:
                # Precisei criar uma classe reset no player
                # para o botão do reset funcionar.
                # world_data = []
                world = reset_level(level_)

                score = 0 # Deletar depois se colocarmos um contador de moeda

                player.reset(88,screen_height - 102)
                game_over = 0

        # If player has completed the lvl
        if game_over == 1:
            # Reset game and go to next level

            level_ += 1
            try:
                if level_ <= max_levels:
                    # Reset level
                    # world_data = []
                    world = reset_level(level_)

                    score = 0 # Deletar depois se colocarmos um contador de moeda

                    player.reset(88,screen_height - 102)
                    game_over = 0
            
            except Exception as e: # Index out of the range if get win all lvls, so, dicided to restart.
                    main_menu == True
                    level_ = 0
                    world = reset_level(level_)

                    score = 0

                    player.reset(88,screen_height - 102)
                    game_over = 0
                    print('Parabéns!!!!!!! Você ganhooou!!') # Podemos fazer um append para
                    # o primeiro level ser uma tela de parabéns!
                    print(e)

            else:
                
                if restart_button.draw():
                    # level = 1

                    world = reset_level(level_)

                    score = 0 # Deletar depois se colocarmos um contador de moeda

                    player.reset(88,screen_height - 102)
                    game_over = 0
                    level_ += 1
                


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()