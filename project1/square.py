import pygame
import numpy as np

class Square:
    def __init__(self, x, y, width, height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.abs_x = x * width
        self.abs_y = y * height
        self.abs_pos = (self.abs_x, self.abs_y)
        self.pos = (x, y)
        self.color='non-playable' if  type == 0 else 'playable'
        self.draw_color = (254, 248, 221) if self.color == 'non-playable' else (254, 230, 227)
        self.highlight_img=pygame.image.load('images/green_ball3.png')
        self.highlight = False
        self.occupying_piece = None
        self.coord = self.get_coord()
        self.rect = pygame.Rect(
            self.abs_x,
            self.abs_y,
            self.width,
            self.height
        )

    # get the formal notation of the tile
    def get_coord(self):
        columns = 'abcdefghijklmnopqrstuvwxyz'
        return columns[self.x] + str(self.y + 1)

    def draw(self, display):
        # configures if tile should be light or dark or highlighted tile
        pygame.draw.rect(display, self.draw_color, self.rect)
        
        # adds the balls icons
        if self.occupying_piece != None:
            centering_rect = self.occupying_piece.img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.occupying_piece.img, centering_rect.topleft)
        
        if self.highlight:
            centering_rect = self.highlight_img.get_rect()
            centering_rect.center = self.rect.center
            display.blit(self.highlight_img, centering_rect.topleft)