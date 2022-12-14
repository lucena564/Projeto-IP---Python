# Classe mais importante, precisa ser um import global.

import os
import pygame
from constants.BackgroundConstants import BackgroundConstants
from classes.enemies.Enemy import Enemy
from classes.sushi.Sushi import Sushi
from classes.exit.Exit import Exit
from classes.lava.Lava import Lava 
from classes.coin.Coin import Coin
from classes.platform.Platform import Platform
from levels.levels_data import *

tile_size = BackgroundConstants.TILE_SIZE

# Todas as novas classes são instaciadas aqui.

blob_group, lava_group, coin_group, exit_group, sushi_power_group, platform_group = pygame.sprite.Group(
), pygame.sprite.Group(), pygame.sprite.Group(),  pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

screen = BackgroundConstants.SCREEN


class World():
    def __init__(self, world_data, image_name):
        self.tile_list = []

        # Dirt
        dirt_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt.png'))
        dirt_alien_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_alien.png'))
        dirt_candy_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_candy.png'))
        dirt_game_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_game.png'))
        dirt_book_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_bookroom.png'))
        dirt_prison_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_prison.png'))
        dirt_garden_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_garden.png'))
        dirt_restaurant_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_restaurant.png'))
        dirt_lava_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_lava.png'))
        dirt_swamp_img = pygame.image.load(os.path.join(
            'assets', 'background', 'dirt_swamp.png'))

        # Grass
        grass_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass.png'))
        grass_alien_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_alien.png'))
        grass_candy_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_candy.png'))
        grass_game_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_game.png'))
        grass_book_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_bookroom.png'))
        grass_prison_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_prison.png'))
        grass_garden_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_garden.png'))
        grass_restaurant_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_restaurant.png'))
        grass_lava_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_lava.png'))
        grass_swamp_img = pygame.image.load(os.path.join(
            'assets', 'background', 'grass_swamp.png'))

        row_count = 0
        for row in world_data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    if image_name == 'alien':
                        img = pygame.transform.scale(
                            dirt_alien_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'candy':
                        img = pygame.transform.scale(
                            dirt_candy_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'gameroom':
                        img = pygame.transform.scale(
                            dirt_game_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'booksroom':
                        img = pygame.transform.scale(
                            dirt_book_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'prison':
                        img = pygame.transform.scale(
                            dirt_prison_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'garden':
                        img = pygame.transform.scale(
                            dirt_garden_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'restaurant':
                        img = pygame.transform.scale(
                            dirt_restaurant_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'swamp':
                        img = pygame.transform.scale(
                            dirt_swamp_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'lava':
                        img = pygame.transform.scale(
                            dirt_lava_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    else:
                        img = pygame.transform.scale(
                            dirt_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                if tile == 2:  # Grama
                    if image_name == 'alien':
                        img = pygame.transform.scale(
                            grass_alien_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'candy':
                        img = pygame.transform.scale(
                            grass_candy_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'gameroom':
                        img = pygame.transform.scale(
                            grass_game_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'booksroom':
                        img = pygame.transform.scale(
                            grass_book_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'prison':
                        img = pygame.transform.scale(
                            grass_prison_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'garden':
                        img = pygame.transform.scale(
                            grass_garden_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'restaurant':
                        img = pygame.transform.scale(
                            grass_restaurant_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'lava':
                        img = pygame.transform.scale(
                            grass_lava_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    elif image_name == 'swamp':
                        img = pygame.transform.scale(
                            grass_swamp_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                    else:
                        img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                        img_rect = img.get_rect()
                        img_rect.x = col_count * tile_size
                        img_rect.y = row_count * tile_size
                        tile = (img, img_rect)
                        self.tile_list.append(tile)

                if tile == 3:  # Para mudarmos o inimigo iremos precisar mexer aqui.
                    # argumentos: Depende da coluna * tile_size, o msm p/ linha
                    blob = Enemy(col_count * tile_size,
                                 row_count * tile_size + 2)

                    blob_group.add(blob)

                if tile == 4:  # horizontal Platform
                    if image_name == 'lava':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform_lava.png')
                        platform_group.add(platform)

                    elif image_name == 'swamp':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform_swamp.png')
                        platform_group.add(platform)

                    elif image_name == 'garden':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform_garden.png')
                        platform_group.add(platform)

                    elif image_name == 'prison':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform_prison.png')
                        platform_group.add(platform)

                    elif image_name == 'booksroom':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform_bookroom.png')
                        platform_group.add(platform)

                    else:
                        platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, 'platform.png')
                        platform_group.add(platform)

                if tile == 5:  # vertical platform
                    if image_name == 'lava':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform_lava.png')
                        platform_group.add(platform)

                    elif image_name == 'swamp':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform_swamp.png')
                        platform_group.add(platform)

                    elif image_name == 'garden':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform_garden.png')
                        platform_group.add(platform)

                    elif image_name == 'prison':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform_prison.png')
                        platform_group.add(platform)

                    elif image_name == 'booksroom':
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform_bookroom.png')
                        platform_group.add(platform)

                    else:
                        platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, 'platform.png')
                        platform_group.add(platform)

                if tile == 6:
                    if image_name == 'garden' or image_name == 'swamp' or image_name == 'alien' or image_name == 'booksroom' or image_name == 'restaurant':
                        lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2), 'lava_blue.png')
                        lava_group.add(lava)
                    else:
                        lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2), 'lava.png')
                        lava_group.add(lava)

                if tile == 7:
                    coin = Coin(col_count * tile_size + (tile_size // 2),
                                row_count * tile_size + (tile_size // 2))
                    coin_group.add(coin)

                if tile == 8:
                    exit_action = Exit(col_count * tile_size,
                                       row_count * tile_size - (tile_size // 2))

                    exit_group.add(exit_action)

                if tile == 9:
                    sushi = Sushi(col_count * tile_size,
                                  row_count * tile_size + (tile_size // 2))
                    sushi_power_group.add(sushi)

                
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

            # Descomentar a linha a baixo para mostrar o grid.
            # pygame.draw.rect(screen, (255, 255, 255), tile[1], 2)
