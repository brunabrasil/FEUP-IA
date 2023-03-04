import pygame
import numpy as np
import os
import platform
from board import Board
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'


board1 = np.array([[0, 0, 0, 3, 3, 3, 0, 0, 0], 
[0, 0, 0, 1, 1, 1, 0, 0, 0], 
[0, 0, 0, 1, 3, 1, 0, 0, 0],
[3, 3, 3, 1, 1, 1, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 2, 2, 2, 3, 3, 3], 
[0, 0, 0, 2, 3, 2, 0, 0, 0], 
[0, 0, 0, 2, 2, 2, 0, 0, 0], 
[0, 0, 0, 3, 3, 3, 0, 0, 0]])

def main():
     
    # initialize the pygame module
    pygame.init() 
    WINDOW_SIZE =(610,610)
    screen = pygame.display.set_mode(WINDOW_SIZE)
    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board1)
    # load and set the logo
    #logo = pygame.image.load("logo.png")
    #pygame.display.set_icon(logo)
    def draw(display):
        display.fill('white')
        board.draw(display)
        pygame.display.update()


    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
    #pygame.Surface.blit(screen, image, (0, 0))
    # main loop
    while running:    
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        draw(screen)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()