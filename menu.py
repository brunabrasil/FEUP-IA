""" 

board1 = [[0, 0, 0, 3, 3, 3, 0, 0, 0], 
[0, 0, 0, 1, 1, 1, 0, 0, 0], 
[0, 0, 0, 1, 3, 1, 0, 0, 0],
[3, 3, 3, 1, 1, 1, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 2, 2, 2, 3, 3, 3], 
[0, 0, 0, 2, 3, 2, 0, 0, 0], 
[0, 0, 0, 2, 2, 2, 0, 0, 0], 
[0, 0, 0, 3, 3, 3, 0, 0, 0]]

board2 = [[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0], 
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0],
[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0]]

board3 = [[0, 0, 0, 0, 3, 3, 3,3, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0]]

def initialBoard(var):
    if(var == 1):
        return board1
    elif(var == 2):
        return board2
    else:
        return board3

def verifyWinner(board, PLAYER_TURN):
    PERCORRER BOARD E VER SE UMA PEÇA NAO SE PODE MOVER

def verifyInput(playerInput,playerTurn):


def verifyMove(move):
    

def verticalMovement(move):
    SOMETHING

def horizontalMovement(move):


PESSOA TEM DE DAR AS COORDENADAS DA PEÇA QUE QUER JOGAR
PESSOAR TEM DE DAR AS COORDENADAS FINAIS DESSA PEÇA
SE NAO DER INDICAR LISTA DE JOGADAS(?)
print(1)
 """
""" 
# import the pygame module, so you can use it
import pygame
import os
import platform
if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'
# define a main function
def main():
     
    # initialize the pygame module
    pygame.init() 
    screen = pygame.display.set_mode((640,640)) 
    # load and set the logo
    #logo = pygame.image.load("logo.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("TES program")
    #image = pygame.image.load("wanaboard2.png").convert_alpha()
    white = (255,255,255)
    black = (18,18,19)
    screen.fill(white)

    # create a surface on screen that has the size of 240 x 180
    
    # define a variable to control the main loop
    running = True
    #pygame.Surface.blit(screen, image, (0, 0))
    # main loop
    pygame.display.update()
    while running:    
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
     
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main() """

