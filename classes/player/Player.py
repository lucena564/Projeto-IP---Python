from os import path
import pygame
from pygame import mixer
from constants.BackgroundConstants import BackgroundConstants
from classes.world.World import blob_group, lava_group, exit_group, coin_group, sushi_power_group, platform_group

screen = BackgroundConstants.SCREEN

screen_height = BackgroundConstants.SCREEN_HEIGHT

pygame.mixer.pre_init(44100, -16, 2, 512) # Peguei essa config na net para rodar a musica direitinho.
mixer.init()

jump_fx = pygame.mixer.Sound(path.join('sound', 'jump.wav'))
jump_fx.set_volume(0.4)
game_over_fx = pygame.mixer.Sound(path.join('sound', 'game_over.wav'))
game_over_fx.set_volume(0.2)
door_fx = pygame.mixer.Sound(path.join('sound', 'Ta-Da-original.wav'))
door_fx.set_volume(0.1)

class Player():
    def __init__(self, x, y):
        self.reset(x,y)

    def update(self, game_over, world_data):
        dx = 0
        dy = 0
        walk_cooldown = 1
        col_thresh = 20

        if game_over == 0:
            # Get keypresses
            key = pygame.key.get_pressed()

            if key[pygame.K_UP] and self.jumped == False and self.in_air == False:
                jump_fx.play() # Pensar como será esse import
                if pygame.sprite.spritecollide(self, sushi_power_group, False):
                    for _duration in range(10):
                     self.vel_y = -30 # Negative move to up
                else:
                 self.vel_y = -15
                self.jumped = True
            
            if key[pygame.K_UP] == False:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1

            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1

            if key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False:
                self.counter = 0
                self.direction = 0
                self.index = 0
                self.image = self.images_right[4]
                # print(self.image)
                # print(self.rect)

            # Handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1

                if self.index >= len(self.images_right) - 1:
                    self.index = 0
                    
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                    
                if self.direction == -1:
                    self.image = self.images_left[self.index]
            
            # Gravity
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Check for Collision
            self.in_air = True
            for tile in world_data.tile_list:
                # Check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # Check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    # Check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0

                    # Check if below the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # Check for Collision with enemies
            if pygame.sprite.spritecollide(self, blob_group, False) and not pygame.sprite.spritecollide(self, sushi_power_group, False):
                game_over_fx.play()
                game_over = -1
                # print(game_over)
            
            # Check for Collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False) and not pygame.sprite.spritecollide(self, sushi_power_group, False):
                game_over_fx.play()
                game_over = -1
                # print(game_over)
            
            # Check for Collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                door_fx.play()
                game_over = 1

            #Check for collision with Platforms
            for platform in platform_group:
                #collision in the x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0
                #collision in the y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if bellow plataform
                    if abs((self.rect.top + dy) - platform.rect.bottom) <  col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top
                    #check if above plataform
                    elif abs((self.rect.bottom +dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    #move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction


            # Update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > -110:
                self.rect.y -= 5

        # Draw player on to screen
        screen.blit(self.image, self.rect)

        return game_over
    
    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0,5):
            img_right = pygame.image.load(f'assets/characters/cat/right{num}_.png')
            img_right = pygame.transform.scale(img_right,(40,45))
            img_left = pygame.transform.flip(img_right,True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.dead_image = pygame.image.load(r'assets/characters/cat_ghost2.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True


