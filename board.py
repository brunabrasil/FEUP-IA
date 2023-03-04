import pygame
import numpy as np
from square import Square
from ball import Ball
class Board:
    def __init__(self, width, height,boardChoosen):
        self.width = width
        self.height = height
        self.tile_width = width // boardChoosen.shape[1] #the tile's size will depend of the board size chosen
        self.tile_height = height // boardChoosen.shape[1]
        self.board = boardChoosen
        self.squares = self.generate_squares()
        self.setup_board()

    def generate_squares(self):
        board = []
        for y in range(self.board.shape[0]):
            for x in range(self.board.shape[0]):
                board.append(
                    Square(x,  y, self.tile_width, self.tile_height, self.board[x][y])
                )
        return board
    

    def get_square_from_pos(self, pos):
        for square in self.squares:
            if (square.x, square.y) == (pos[0], pos[1]):
                return square
            
    def get_piece_from_pos(self, pos):
        return self.get_square_from_pos(pos).occupying_piece
    

    def setup_board(self):
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                if piece != 0 and piece != 3:
                    square = self.get_square_from_pos((x, y))
                    # looking inside contents, what piece does it have
                    if piece == 1: #Player 1 is the blue ball
                        square.occupying_piece = Ball(
                            (x, y), 'blue', self
                        )
                    # as you notice above, we put `self` as argument, or means our class Board
                    elif piece == 2: # Player 2 is the green ball
                        square.occupying_piece = Ball(
                            (x, y), 'green', self
                        )

    def draw(self, display):
        #if self.selected_piece is not None:
         #   self.get_square_from_pos(self.selected_piece.pos).highlight = True
          #  for square in self.selected_piece.get_valid_moves(self):
           #     square.highlight = True
        for square in self.squares:
            square.draw(display)