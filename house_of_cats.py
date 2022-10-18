import pygame

import pickle
from os import path

from classes.button.Button import Button 

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('House of cats')

# Define game variable
tile_size = 50
game_over = 0
main_menu = True
level = 0
max_levels = 7 # Muda dependendo dos mapas

# load images
sun_img = pygame.image.load('img\sun.png')
bg_img = pygame.image.load('img\sky.png')
restart_img = pygame.image.load(r'img\restart_btn.png')
start_img = pygame.image.load(r'img\start_btn.png')
exit_img = pygame.image.load(r'img\exit_btn.png')

def draw_grid(): # Just to call the lines
    for line in range(0,20): # 20
        pygame.draw.line(screen, (255,255,255), (0,line*tile_size), (screen_width, line*tile_size))
        pygame.draw.line(screen, (255,255,255), (line*tile_size,0), (line*tile_size, screen_height))

def reset_level(level):
    player = Player(88,screen_height - 102)
    blob_group.empty()
    lava_group.empty()
    exit_group.empty()

    # Load in level data and create world
    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world




class World():
    def __init__(self, data):
        self.tile_list = []


        # Load images
        dirt_img = pygame.image.load('img/dirt.png')
        grass_img = pygame.image.load('img/grass.png')
        # lava_img = pygame.image.load('img/lava.png')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1: 
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 2: # Grama
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)

                if tile == 3: # Para mudarmos o inimigo iremos precisar mexer aqui.
                    blob = Enemy(col_count * tile_size, row_count * tile_size + 15) # argumentos: Depende da coluna * tile_size, o msm p/ linha  
                    blob_group.add(blob)

                if tile == 6:
                    lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2))
                    lava_group.add(lava)

                if tile == 8:
                    exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    exit_group.add(exit)
                    


                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen,(255,255,255), tile[1], 2)
           
class Enemy(pygame.sprite.Sprite): # Esse parametro é para estilo de jogo sprite (como o nosso)
    # Dentro desse método 'pygame.sprite.Sprite' já temos um método "draw" p/ aparecer o nosso inimigo.
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self) # É uma função do pygame para inimigos.
        self.image = pygame.image.load('img/blob.png') # Trocar por um cachorro
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

class Lava(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/lava.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0    

class Exit(pygame.sprite.Sprite):
    def __init__(self, x, y): 
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/exit.png')
        self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0    


# world_data = [
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
# [1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 2, 2, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 7, 0, 5, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1], 
# [1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
# [1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 7, 0, 0, 0, 0, 2, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
# [1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
# [1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

player = Player(88,screen_height - 102)

blob_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()

# Load in lvl data and create world
if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
    
    world_data = pickle.load(pickle_in)
    
world = World(world_data)

# Create buttons
restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_img)
start_button = Button(screen_width // 2 - 350, screen_height // 2, start_img)
exit_button = Button(screen_width // 2 + 150, screen_height // 2, exit_img)


run = True

# All game run here.
while(run == True):
    
    clock.tick(fps)

    # Tela base do jogo. Colocaremos algumas condições no futuro para o plano de fundo mudar com o nível.
    screen.blit(bg_img, (0,0))
    screen.blit(sun_img, (100,100))

    if main_menu == True:
        if exit_button.draw() == True:
            run = False

        if start_button.draw() == True:
            main_menu = False

    else:

        world.draw()

        if game_over == 0:
            blob_group.update()
        
        blob_group.draw(screen)
        lava_group.draw(screen)
        exit_group.draw(screen)

        game_over = player.update(game_over)

        # If player died
        if game_over == -1:
            if restart_button.draw() == True:
                # Precisei criar uma classe reset no player
                # para o botão do reset funcionar.
                world_data = []
                world = reset_level(level)
                player.reset(88,screen_height - 102)
                game_over = 0

        # If player has completed the lvl
        if game_over == 1:
            # Reset game and go to next level
            level += 1
            if level <= max_levels:
                # Reset level
                world_data = []
                world = reset_level(level)
                player.reset(88,screen_height - 102)
                game_over = 0

            else:
                if restart_button.draw():
                    level = 1

                    world_data = []
                    world = reset_level(level)
                    player.reset(88,screen_height - 102)
                    game_over = 0


                
        # draw_grid() # malha 100x100 - Alterar em title_size == 100 para = 10x10.

        # print(world.tile_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()