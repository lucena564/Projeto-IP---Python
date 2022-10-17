import os
import pygame
from constants.BackgroundConstants import BackgroundConstants
from classes.world.World import World

screen = BackgroundConstants.SCREEN
world = World()

screen_height = BackgroundConstants.SCREEN_HEIGHT

class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(0,5):
            img_right = pygame.image.load(os.path.join('assets','characters','cat', f'right{num}.png'))
            # img_right = pygame.transform.scale(img_right,(135,85)) # img_right = pygame.transform.scale(img_right,(75,65))
            img_right = pygame.transform.scale(img_right,(40,45))
            img_left = pygame.transform.flip(img_right,True, False)
            # img_left = pygame.image.load(f'img/cat/left{num}.png')
            # img_left = pygame.transform.scale(img_left,(135,85))
            
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0

    def update(self):
        dx = 0
        dy = 0
        flag_front = False
        walk_cooldown = 1

        # Get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.jumped == False:
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
        for tile in world.tile_list:
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

        # Update player coordinates
        self.rect.x += dx
        self.rect.y += dy
        
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

        # Draw player on to screen
        screen.blit(self.image, self.rect)
        pygame.draw.rect(screen,(255,255,255), self.rect,1)
