import pygame
import numpy as np
import os
import platform
import time
from board import Board
import pygame_menu

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
    global redType
    global blueType
    global difficulty
    global actualsize
    redType ="human"
    blueType="human"
    difficulty = "easy"
    board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1],board1,redType,blueType, difficulty)
    actualsize=1
    
    def start_with_mode():
        global redType
        global blueType
        global board
        global actualsize
        global difficulty
        if actualsize == 1:
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board1, redType, blueType, difficulty)
        elif actualsize == 2:   
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board2, redType, blueType, difficulty)
        elif actualsize == 3:
            board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board3, redType, blueType, difficulty)
        difficultymenu.disable()
        submenu.disable()
        mainmenu.disable()
    
    def start_the_game():
        global redType
        global blueType
        if(redType=="computer" or blueType=="computer"):
            submenu._open(difficultymenu)
        else:
            global board
            global actualsize
            if actualsize == 1:
                board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board1, redType, blueType,difficulty)
            elif actualsize == 2:   
                board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board2, redType, blueType,difficulty)
            elif actualsize == 3:
                board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1], board3, redType, blueType,difficulty)
            submenu.disable()
            mainmenu.disable()
    
    def level_menu():
        mainmenu._open(submenu)
    
    def set_size(value, size):
        print(value)
        global actualsize 
        actualsize = size
        
    def set_mode(value, mode):
        global redType
        global blueType
        if mode == 1:
            redType = "human"
            blueType = "human"
        if mode==2:
            redType="human"
            blueType="computer"
        if mode==3:
            redType="computer"
            blueType="computer"
    
    def set_difficulty(value, diff):
        global difficulty
        if diff == 1:
            difficulty = "easy"
        if diff == 2:
            difficulty = "hard"    
        
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
    
    difficultymenu = pygame_menu.Menu('Choose computer difficulty', 610, 610, theme=mytheme)
    difficultymenu.add.selector('Computer Difficulty:', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
    difficultymenu.add.button('Start Game', start_with_mode)

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
        print("Board Turn")
        print(board.turn)
        if board.turn == "red" and redType == "computer":
            board.computer_move()
        elif board.turn == "blue" and blueType == "computer":
            board.computer_move()
            
        for event in events:
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                # If the mouse is clicked
                if event.button == 1:
                    if (board.turn == "red" and redType == "human") or (board.turn == "blue" and blueType == "human"):
                        if not board.handle_click(mx, my):
                            running=False
                        print(board.matrix)
            
        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(screen)
            if (mainmenu.get_current().get_selected_widget()):
                arrow.draw(screen, mainmenu.get_current().get_selected_widget())
 
        draw(screen)
    if board.turn == 'blue':
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over! Red player won', True, (255, 255, 255))
    elif board.turn == 'red':
        screen.fill((85, 203, 205))
        font = pygame.font.SysFont('arial', 40)
        title = font.render('Game Over! Blue player won', True, (255, 255, 255))
        
    screen.blit(title, (610/2 - title.get_width()/2, 610/2 - title.get_height()/3))
    pygame.display.update()
    time.sleep(2)

     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()