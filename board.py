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

    def copy(self,new_matrix=None):
        #print("Entrou na copy")
        copyobj = Board()
        for name, attr in self.__dict__.items():
            #print("Name: ",name)
            if hasattr(attr, 'copy') and callable(getattr(attr, 'copy')):
                #print("Copy normal")
                #print(attr)
                if(name=="matrix" and new_matrix is not None):
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
        
        elif self.computerDifficulty=="medium":
            print("Turn before computer move:",self.turn)
            mcts=WanaMCTS(self,self.turn,3)
            piece_and_move=mcts.search()
            print(piece_and_move)
            self=piece_and_move[0].occupying_piece.experimental_move(self,piece_and_move[1])

            
        elif self.computerDifficulty=="hard":
            self=execute_minimaxAlphaBeta_move(Board.evaluate,1,self)
            #self=execute_minimaxNormal_move(Board.evaluate,1,self)

            
        print("Board turn after computer move")
        print(self.turn)
        return self
    


class WanaNode:
    def __init__(self, board, turn,parent=None):
        self.board = board.copy()
        self.turn = turn
        self.children = []
        self.visits = 0
        self.wins = 0
        self.parent=parent
        self.last_piece_and_move=(None,None)
        
#
    def expand(self):
        for piece in self.board.get_pieces():
            for move in piece.occupying_piece.get_moves(self.board):
                next_board = piece.occupying_piece.experimental_move(self.board,move)
                child = WanaNode(next_board, self.turn,self)
                self.children.append(child)

    def select(self):
        c = 1.4
        total_visits = sum(child.visits for child in self.children)
        print("TOTAL VISITS:",total_visits)
        log_total_visits = math.log(total_visits) if total_visits > 0 else 1

        best_score = float('-inf')
        best_child = None

        for child in self.children:
            if child.visits == 0:
                score = float('inf')
            else:
                exploitation = child.wins / child.visits
                exploration = c * math.sqrt(log_total_visits / child.visits)
                score = exploitation + exploration

            if score > best_score:
                best_score = score
                best_child = child

        return best_child


    def simulate(self):
        print("IN simulate")
        print("SElf turn:",self.turn)
        board = self.board.copy()
        board.turn = self.turn
        last_piece=None
        last_move=None
        print("Board turn:",board.turn)
        moves=[]
        while True:
            if(board.check_gameover(board.turn)):
                break
            
            pieces=board.get_pieces()
            random_piece=pieces[np.random.randint(0,len(pieces))]
            #print("Random piece color:",random_piece.occupying_piece.color)
            random_move_list=random_piece.occupying_piece.get_moves(board)
            random_move=random_move_list[np.random.randint(0,len(random_move_list))]
            board=random_piece.occupying_piece.experimental_move(board,random_move)
            
            if(last_piece is None and last_move is None):
                last_piece=random_piece
                last_move=random_move
        
        #!!!!!!!!!!
        print("Last piece and move:", last_piece.occupying_piece.color, last_move.occupying_piece.color)
        self.last_piece_and_move=(last_piece,last_move)
        return board.turn != self.turn

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
                print("A ir para o select")
                node = node.select()
                print("Saiu do select caraca")
            if node.visits == 0:
                node.expand()
            result = node.simulate()
            print("Node last_piece_and_move",node.last_piece_and_move)
            node.backpropagate(result)

        best_child = max(self.root.children, key=lambda child: child.visits)
        print("Best child", best_child)
        return best_child.last_piece_and_move







