from os import path
import pygame
from pygame import mixer
from constants.BackgroundConstants import BackgroundConstants
from classes.button.Button import Button

from classes.player.Player import Player
from classes.coin.Coin import Coin
from classes.world.World import World, blob_group, lava_group, exit_group, coin_group, sushi_power_group, platform_group

from levels.levels_data import next_level_array

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (230, 97, 29)


tile_size = BackgroundConstants.TILE_SIZE

screen_width = BackgroundConstants.SCREEN_WIDTH
screen_height = BackgroundConstants.SCREEN_HEIGHT

screen = BackgroundConstants.SCREEN

# FUNÇÕES
def count_coins_level(world_data):
    counter_coins = 0
    for line in world_data:
        for number in line:
            if number == 7:
                counter_coins += 1
    return counter_coins


def draw_grid(screen, tile_size, screen_width, screen_height):  # Just to call the lines
    for line in range(0, 20):  # 20
        pygame.draw.line(screen, (255, 255, 255),
                         (0, line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255, 255, 255),
                         (line*tile_size, 0), (line*tile_size, screen_height))


def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def reset_level(level, tile_size):
    blob_group.empty()
    lava_group.empty()
    coin_group.empty()
    exit_group.empty()
    platform_group.empty()
    coin_group.empty()
    sushi_power_group.empty()

    score_coin = Coin((tile_size // 2) + 50, (tile_size // 2) + 0)
    coin_group.add(score_coin)
    world_data = next_level_array[level][0]
    image_name = next_level_array[level][2]
    world = World(world_data, image_name)

    return world

# Configuração padrão para os efeitos sonoros (Não mexer aqui.)
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
# Fim

clock = pygame.time.Clock()
font_miau = pygame.font.SysFont("Bauhaus 93", 70)
font_miau_endgame = pygame.font.SysFont("Bauhaus 93", 60)
font_score = pygame.font.SysFont('Bauhaus 93', 30)

fps = 60
game_over = 0
main_menu = True
max_levels = len(next_level_array)
num_coins_level = 0
score = 0
zerou_jogo = False

pygame.display.set_caption('Catify: The World')

restart_img = pygame.image.load(path.join('assets', 'menu', 'restart_btn.png'))
start_img = pygame.image.load(path.join('assets', 'menu', 'start_btn.png'))
exit_img = pygame.image.load(path.join('assets', 'menu', 'exit_btn.png'))

restart_button = Button(screen_width // 2 - 50,
                            screen_height // 2 + 100, restart_img)
restart_button_running_level = Button(50, 50, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)

# Load sounds
coin_fx = pygame.mixer.Sound(path.join('sound', 'comic_lick.wav'))
coin_fx.set_volume(0.05)

# Creating a static coin for score - Had to import Coin class.
score_coin = Coin((tile_size // 2) + 50, (tile_size // 2) + 0)
coin_group.add(score_coin)


level_ = 0
world_data = next_level_array[level_][0]
num_coins_level = count_coins_level(world_data)
image_name = next_level_array[level_][2]
world = World(world_data, image_name)

player = Player(88, screen_height - 102)


run = True

# All game is ran here.
while (run == True):

        clock.tick(fps)
        screen.blit(next_level_array[level_][1], (0, 0))

        if main_menu == True:

            if zerou_jogo:
                draw_text(screen, 'VOCÊ ZEROU O JOGO MIAUMIGO!', font_miau_endgame, orange,
                        170, 300)
                draw_text(screen, 'Deseja uma nova Gatoventura?', font_miau_endgame, orange,
                        195, 350)

            if exit_button.draw() == True:
                run = False

            if start_button.draw() == True:
                main_menu = False
                zerou_jogo = False

        else:

            world.draw()
            draw_text(screen, ' X ' + str(score), font_score, black, tile_size + 40, 17)

            if game_over == 0:
                if restart_button_running_level.draw() == True:
                    world = reset_level(level_,tile_size)
                    score = 0
                    player.reset(88, screen_height - 102)

                blob_group.update()
                platform_group.update()
                sushi_power_group.update()

                # Update score
                # Check if a coin has been collected
                # True parameter is to colect the coin and hide it inside the map.
                for coin in coin_group:
                    if pygame.sprite.collide_rect(player, coin):
                        coin_fx.play()
                        coin.remove(coin_group)
                        score += 1
                        if (score == num_coins_level):
                            player.collected_all_coins = True


            blob_group.draw(screen)
            platform_group.draw(screen)
            lava_group.draw(screen)
            coin_group.draw(screen)
            sushi_power_group.draw(screen)
            exit_group.draw(screen)

            game_over = player.update(game_over, world)

            # If player died
            if game_over == -1:
                draw_text(screen, 'Miaaaaaaaau!!! >:(', font_miau, red,
                        (screen_width // 2) - 250, screen_height // 2)
                if restart_button.draw() == True:
                    # Foi criado uma classe reset no player
                    # para o botão do reset funcionar.
                    # world_data = []
                    world = reset_level(level_, tile_size)
                    score = 0  # Deletar depois se colocarmos um contador de moeda
                    player.reset(88, screen_height - 102)
                    game_over = 0

            # If player has completed the lvl
            if game_over == 1:
                # Reset game and go to next level

                level_ += 1
                try:
                    if level_ <= max_levels:
                        # Reset level
                        num_coins_level = count_coins_level(
                            next_level_array[level_][0])
                        world = reset_level(level_, tile_size)
                        score = 0  # Deletar depois se colocarmos um contador de moeda
                        player.reset(88, screen_height - 102)
                        game_over = 0

                # Index out of the range if get win all lvls, so, dicided to restart.
                except Exception as e:
                    main_menu = True
                    level_ = 0
                    num_coins_level = count_coins_level(
                        next_level_array[level_][0])
                    world = reset_level(level_, tile_size)

                    score = 0

                    player.reset(88, screen_height - 102)
                    game_over = 0
                    zerou_jogo = True
                    print(e)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
pygame.quit()