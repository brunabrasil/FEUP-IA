import pygame
import numpy as np
import os
import platform
import time
from board import Board
import pygame_menu
from pygame_menu import themes

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
    global board
    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board1)
    def start_the_game():
        submenu.disable()
        mainmenu.disable()
    
    def level_menu():
        mainmenu._open(submenu)
    
    def set_size(value, size):
        print(value)
        global board
        if size == 1:
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board1)
        elif size == 2:
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board2)
        elif size == 3:
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board3)

        print(size)
        
    def set_mode(value, mode):
        print(value)
        print(mode)
 
    mytheme = pygame_menu.themes.THEME_BLUE.copy()
    mytheme.cursor_selection_color=(85, 203, 205)
    mytheme.title_font_shadow = False
    mytheme.title_font = pygame_menu.font.FONT_BEBAS
    mainmenu = pygame_menu.Menu('WANA', 610, 610, theme=mytheme)
    mainmenu.add.button('Play', level_menu)
    mainmenu.add.button('Instructions', level_menu)
    mainmenu.add.button('Quit', pygame_menu.events.EXIT)
    
    submenu = pygame_menu.Menu('Game Options', 610, 610, theme=mytheme)
    submenu.add.selector('Mode: ', [('Player vs Player', 1), ('Player vs Computer', 2), ('Computer vs Computer', 3)], onchange=set_mode)
    submenu.add.selector('Board Size:', [('Small', 1), ('Medium', 2), ('Large', 3)], onchange=set_size)
    submenu.add.button('Start Game', start_the_game)
    mainmenu.mainloop(screen)

    # load and set the logo
    #logo = pygame.image.load("logo.png")
    #pygame.display.set_icon(logo)
    def draw(display):
        color=(254, 248, 221)
        display.fill(color)
        board.draw(display)
        pygame.display.update()

    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size = (10, 15))
 
    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        events = pygame.event.get()
        for event in events:
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                # If the mouse is clicked
                if event.button == 1:
                    if not board.handle_click(mx, my):
                        running=False
            
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(screen)
            if (mainmenu.get_current().get_selected_widget()):
                arrow.draw(screen, mainmenu.get_current().get_selected_widget())
 
        draw(screen)

    time.sleep(1)
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()