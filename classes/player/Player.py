import os
import pygame
from constants.BackgroundConstants import BackgroundConstants
from classes.world.World import World

screen = BackgroundConstants.SCREEN

screen_height = BackgroundConstants.SCREEN_HEIGHT

blob_group, lava_group, exit_group = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()


class Player():
    def __init__(self, x, y):
        self.reset(x,y)
        # self.images_right = []
        # self.images_left = []
        # self.index = 0
        # self.counter = 0
        # for num in range(0,5):
        #     img_right = pygame.image.load(f'img/cat/right{num}.png')
        #     # img_right = pygame.transform.scale(img_right,(135,85)) # img_right = pygame.transform.scale(img_right,(75,65))
        #     img_right = pygame.transform.scale(img_right,(40,45))
        #     img_left = pygame.transform.flip(img_right,True, False)
        #     # img_left = pygame.image.load(f'img/cat/left{num}.png')
        #     # img_left = pygame.transform.scale(img_left,(135,85))
            
        #     self.images_right.append(img_right)
        #     self.images_left.append(img_left)

        # self.dead_image = pygame.image.load(r'img\ghost.png')
        # self.image = self.images_right[self.index]
        # self.rect = self.image.get_rect()
        # self.rect.x = x
        # self.rect.y = y
        # self.width = self.image.get_width()
        # self.height = self.image.get_height()
        # self.vel_y = 0
        # self.jumped = False
        # self.direction = 0

    def update(self, game_over, world_data):
        dx = 0
        dy = 0
        walk_cooldown = 1

        if game_over == 0:
            # Get keypresses
            key = pygame.key.get_pressed()
            if key[pygame.K_UP] and self.jumped == False and self.in_air == False:
                self.vel_y = -15 # Negative move to up
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
            
            # Add gravity
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
            if pygame.sprite.spritecollide(self, blob_group, False):
                game_over = -1
                # print(game_over)
            
            # Check for Collision with lava
            if pygame.sprite.spritecollide(self, lava_group, False):
                game_over = -1
                # print(game_over)

            # Check for Collision with exit
            if pygame.sprite.spritecollide(self, exit_group, False):
                game_over = 1

                
                    
            # Update player coordinates
            self.rect.x += dx
            self.rect.y += dy

        elif game_over == -1:
            self.image = self.dead_image
            if self.rect.y > 200:
                self.rect.y -= 5
        
        # if self.rect.bottom > screen_height:
        #     self.rect.bottom = screen_height

        # Draw player on to screen
        screen.blit(self.image, self.rect)
        # pygame.draw.rect(screen,(255,255,255), self.rect,1)

        return game_over
    
    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0,5):
            img_right = pygame.image.load(f'assets/characters/cat/right{num}.png')
            # img_right = pygame.transform.scale(img_right,(135,85)) # img_right = pygame.transform.scale(img_right,(75,65))
            img_right = pygame.transform.scale(img_right,(40,45))
            img_left = pygame.transform.flip(img_right,True, False)
            # img_left = pygame.image.load(f'img/cat/left{num}.png')
            # img_left = pygame.transform.scale(img_left,(135,85))
            
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.dead_image = pygame.image.load(r'assets\characters\ghost.png')
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
