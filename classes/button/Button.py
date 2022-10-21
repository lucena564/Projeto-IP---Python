import pygame
from constants.BackgroundConstants import BackgroundConstants

screen = BackgroundConstants.SCREEN

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False

        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Check mouseover and clicked conditions
        if self.rect.collidepoint(pos) == True:
            # print('O mouse está em cima do botão.')
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # [0] indica botão esquerdo do mouse.
                action = True # print('Botão direito clicado.')
                self.clicked = True

        # Sem essa função iria dar spam click.
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
                
        # Draw button
        screen.blit(self.image, self.rect)
        return action