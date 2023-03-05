import pygame
import numpy as np
import os
import platform
import time
from board import Board
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'


board1 = np.array([
[0, 0, 0, 1, 3, 1, 0, 0, 0], 
[0, 0, 0, 1, 3, 1, 0, 0, 0], 
[0, 0, 0, 1, 3, 1, 0, 0, 0],
[3, 3, 3, 1, 3, 1, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 2, 3, 2, 3, 3, 3], 
[0, 0, 0, 2, 3, 2, 0, 0, 0], 
[0, 0, 0, 2, 3, 2, 0, 0, 0], 
[0, 0, 0, 2, 3, 2, 0, 0, 0]])

board2 = np.array(
[[0, 0, 0, 0, 1, 3, 3,1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 3, 3,1, 0, 0, 0, 0], 
[0, 0, 0, 0, 1, 3, 3,1, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 3, 3,1, 0, 0, 0, 0],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 2, 3, 3,2, 0, 0, 0, 0], 
[0, 0, 0, 0, 2, 3, 3,2, 0, 0, 0, 0], 
[0, 0, 0, 0, 2, 3, 3,2, 0, 0, 0, 0],
[0, 0, 0, 0, 2, 3, 3,2, 0, 0, 0, 0]])

board3 = np.array(
[[0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 1, 3, 3, 3, 1, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 2, 3, 3, 3, 2, 0, 0, 0, 0, 0]])

def main():
     
    # initialize the pygame module
    pygame.init() 
    WINDOW_SIZE =(610,610)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board2)
    # load and set the logo
    #logo = pygame.image.load("logo.png")
    #pygame.display.set_icon(logo)
    def draw(display):
        color=(254, 248, 221)
        display.fill(color)
        board.draw(display)
        pygame.display.update()


    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                # If the mouse is clicked
                if event.button == 1:
                    if not board.handle_click(mx, my):
                        
                        running=False
        draw(screen)
    
    time.sleep(1)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()