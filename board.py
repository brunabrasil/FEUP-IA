import pygame
import numpy as np
import time
import copy
from minimax import execute_minimaxAlphaBeta_move, execute_minimaxNormal_move
from square import Square
from ball import Ball
import random
import math

class Board:
    def __init__(self, width=None, height=None,boardChoosen=None, redType=None, blueType=None,difficulty=None):
        if(width is not None):
            self.width = width
            self.height = height
            self.tile_width = width // boardChoosen.shape[1] #the tile's size will depend of the board size chosen
            self.tile_height = height // boardChoosen.shape[1]
            self.selected_piece = None
            self.matrix = boardChoosen
            self.div=boardChoosen.shape[1]//3
            self.redPlayerType=redType
            self.bluePlayerType=blueType
            self.computerDifficulty=difficulty
            self.turn = 'red'
            self.squares = self.generate_squares()
            self.setup_board()

    def copy(self,new_matrix):
        #print("Entrou na copy")
        copyobj = Board()
        for name, attr in self.__dict__.items():
            #print("Name: ",name)
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                #print("Copy normal")
                #print(attr)
                if(name=="matrix"):
                    #print("ENTERED MATRIx")
                    copyobj.__dict__[name] = new_matrix
                    #print(new_matrix)
                    #print("-.-.-.-.-")
                else: 
                    copyobj.__dict__[name] = attr.copy()
            else:
                #print("Deepcopy")
                copyobj.__dict__[name] = copy.deepcopy(attr)
                
        copyobj.squares = copyobj.generate_squares()
        copyobj.setup_board()

        return copyobj

    def generate_squares(self):
        board = []
        for y in range(self.matrix.shape[0]):
            for x in range(self.matrix.shape[0]):
                board.append(
                    Square(x,  y, self.tile_width, self.tile_height, self.matrix[x][y])
                )
        return board
    

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    

    def setup_board(self):
        for y, row in enumerate(self.matrix):
            for x, piece in enumerate(row):
                if piece != 0:
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece == 1: #Player 1 is the blue ball
                        square.occupying_piece = Ball(
                            (x, y), 'blue', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece == 2: # Player 2 is the green ball
                        square.occupying_piece = Ball(
                            (x, y), 'red', self
                        )
                    elif piece==3:
                        square.occupying_piece = Ball(
                            (x, y), 'white', self
                        )

    def draw(self, display):
        if self.selected_piece is not None:
            #self.get_square_from_pos(self.selected_piece.pos).highlight = True
          #  print(list)
            for square in self.selected_piece.get_moves(self):
                #print(square)
                square.highlight = True
        for square in self.squares:
            square.draw(display)

    def handle_click(self, mx, my):
        x = mx // self.tile_width
        y = my // self.tile_height
        clicked_square = self.get_square_from_pos((x, y))
        #print(clicked_square.x, clicked_square.y)
        if self.selected_piece is None:
            if clicked_square.occupying_piece is not None:
                if clicked_square.occupying_piece.color == self.turn:
                    self.selected_piece = clicked_square.occupying_piece 
        elif self.selected_piece.move(self, clicked_square):
            self.turn = 'blue' if self.turn == 'red' else 'red'
            if self.check_gameover(self.turn):
                print("Game Over")
                return False
        return True   
        
        

    def check_gameover(self,color):
        output = False
        
        for piece in [i.occupying_piece for i in self.squares]:
            if piece != None:
                if piece.get_moves(self) == [] and piece.color==color:
                    output = True
                    
        return output 

    # get pieces of a certain player
    def get_pieces(self):
        pieces = []
        for square in self.squares:
            if square.occupying_piece is not None:
                if square.occupying_piece.color == self.turn:
                    pieces.append(
                        square
                    )
        return pieces

    def evaluate(board):
        red_score=0
        blue_score=0
        
        for square in board.squares:
            if square.occupying_piece is not None:
                if square.occupying_piece.color=='red':
                    red_score+=len(square.occupying_piece.get_moves(board))
                elif square.occupying_piece.color=='blue':
                    blue_score+=len(square.occupying_piece.get_moves(board))
        
        if board.turn=='red':
            return -blue_score
        
        # Blue turn
        return -red_score
    
    
    
    
    def computer_move(self):
        print("In computer move")
        print(self.turn)
        time.sleep(1)
        if self.computerDifficulty=="easy":
            
            pieces_list=self.get_pieces()
            random_piece=pieces_list[np.random.randint(0,len(pieces_list))]
            random_move_list=random_piece.occupying_piece.get_moves(self)
            random_move=random_move_list[np.random.randint(0,len(random_move_list))]
            self=random_piece.occupying_piece.experimental_move(self,random_move)
            print("Buscando o inseto")
            print(self.matrix)
            self.squares = self.generate_squares()
            self.setup_board()
            
        elif self.computerDifficulty=="hard":
            self=execute_minimaxAlphaBeta_move(Board.evaluate,2,self)
            #self=execute_minimaxNormal_move(Board.evaluate,1,self)
        
        print("Board turn after computer move")
        print(self.turn)
        return self
    


class WanaNode:
    def __init__(self, board, turn):
        self.board = board
        self.turn = turn
        self.children = []
        self.visits = 0
        self.wins = 0

    def expand(self):
        for move in self.board.get_possible_moves(self.turn):
            next_board = self.board.move(move, self.turn)
            next_turn = self.board.get_next_turn(self.turn)
            child = WanaNode(next_board, next_turn)
            self.children.append(child)

    def select(self):
        c = 1.4
        total_visits = sum(child.visits for child in self.children)
        log_total_visits = math.log(total_visits)

        best_score = float('-inf')
        best_child = None

        for child in self.children:
            exploitation = child.wins / child.visits
            exploration = c * math.sqrt(log_total_visits / child.visits)
            score = exploitation + exploration

            if score > best_score:
                best_score = score
                best_child = child

        return best_child

    def simulate(self):
        board = self.board.copy()
        turn = self.turn
        while True:
            moves = board.get_legal_moves(turn)
            if not moves:
                break
            move = random.choice(moves)
            board = board.move(move, turn)
            turn = board.get_next_turn(turn)
        return board.get_winner() == self.turn

    def backpropagate(self, result):
        self.visits += 1
        self.wins += result
        if self.parent:
            self.parent.backpropagate(result)

class WanaMCTS:
    def __init__(self, board, turn, max_simulations):
        self.root = WanaNode(board, turn)
        self.max_simulations = max_simulations

    def search(self):
        for i in range(self.max_simulations):
            node = self.root
            while node.children:
                node = node.select()
            if node.visits == 0:
                node.expand()
            result = node.simulate()
            node.backpropagate(result)

        best_child = max(self.root.children, key=lambda child: child.visits)
        return best_child.board.last_move







