import pygame
import copy


class Ball:
    def __init__(self, pos, color, board):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.color = 'white'
        self.img = pygame.image.load('images/white_ball.png') 
        if color == 'blue':
            self.color='blue' 
            self.img=pygame.image.load('images/blue_ball.png')
        elif color=='red':
            self.color='red'
            self.img=pygame.image.load('images/red_ball.png')
        self.has_moved = False
        
    def get_moves(self, board):
        output = []
        white= (255,255,255)
        for direction in self.get_possible_moves(board):
            for square in direction:
                output.append(square)
                    #break
                
        #print('Final')
        #print(output)
        return output
    
    def moves_up_straight(self,board):
        moves=[]
        #print('In up_straight')
        if self.x>=board.div and self.x<board.matrix.shape[1]-board.div :
 
            for i in range(self.y - 1, -1, -1):
                #print(i)
                square = board.get_square_from_pos((self.x, i))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        #print('Nao foi branco 1')
                        #print(square.occupying_piece.color)
                        #print(moves)
                        return moves
                    else:
                        #print('Chegueiiiii')
                        moves.append(square) 
                        #print(moves) 

            #print('In second for up_straight')
            for i in range(board.matrix.shape[1]-1, self.y,-1):
                square = board.get_square_from_pos((self.x, i))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        #print(square.occupying_piece.color)
                        return moves
                    moves.append(square)  
        
        return moves
    
    def moves_down_straight(self,board):
        moves=[]
        #print('In down_straight')
        if self.x>=board.div and self.x<board.matrix.shape[1]-board.div :
            for y in range(self.y + 1, board.matrix.shape[1]):
                square = board.get_square_from_pos((self.x, y))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        #print('Nao foi branco')
                        #print(square.occupying_piece.color)
                        return moves
                    #print(square.occupying_piece.color)
                    moves.append(square) 
        
            for y in range(0, self.y):
                square =board.get_square_from_pos((self.x, y))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        #print('Nao foi branco')
                        #print(square.occupying_piece.color)
                        return moves
                    #print(square.occupying_piece.color)
                    moves.append(square)    
        
        return moves
    
        
    def moves_right_straight(self,board):
        moves = []
        if self.y>=board.div and self.y<board.matrix.shape[1]-board.div :
            for x in range(self.x + 1, board.matrix.shape[1]):
                square = board.get_square_from_pos((x, self.y))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        return moves
                    moves.append(square)
                
            for x in range(0, self.x):
                square = board.get_square_from_pos((x, self.y))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        return moves
                    moves.append(square)
            
        return moves
    
    def moves_left_straight(self,board):
        moves = []
        if self.y>=board.div and self.y<board.matrix.shape[1]-board.div :
            for x in range(self.x)[::-1]:
                square = board.get_square_from_pos((x, self.y))
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        return moves
                    moves.append(square)
            
            for x in range(board.matrix.shape[1] - 1, self.x, -1):
                square = board.get_square_from_pos((x, self.y))
                #print(self.x)
                if square.occupying_piece is not None:
                    if square.occupying_piece.color != 'white':
                        return moves
                    moves.append(square)
                
        return moves
    
    def aux_curve_moves(self,board,top_row,right_column,bottom_row,left_column):
        moves_temp=[]
        
        for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((i, top_row))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
        
        for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((right_column,i))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
                        
        for i in range(2*board.div-1,board.div-1,-1):
                square=board.get_square_from_pos((i,bottom_row))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
        
        for i in range(2*board.div-1,board.div-1,-1):
                square=board.get_square_from_pos((left_column,i))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
        
        #print(moves_temp)
        return moves_temp
    
    def moves_clockwise(self,board):
        moves=[]
        moves_temp=[]
        #print(self.x,self.y)
        #head or bottom
        if self.y>=board.matrix.shape[1]-board.div or self.y<board.div :
            #print('head or bottom')
            # top row
            top_row=self.y if self.y<board.div else board.matrix.shape[1]-1-self.y
            #right column
            right_column=max(self.y,board.matrix.shape[1]-1-self.y)          
            #bottom row
            bottom_row=board.matrix.shape[1]-1-self.y if self.y<board.div else self.y            
            #left column
            left_column=min(self.y,board.matrix.shape[1]-1-self.y)
  
            
         
        #right and left arms
        elif self.x>=board.matrix.shape[1]-board.div or self.x<board.div :
            #print('right and left arms')
            # top row
            top_row=min(self.x,board.matrix.shape[1]-1-self.x)            
            # right column
            right_column=self.x if self.x>board.div else board.matrix.shape[1]-1-self.x         
            #bottom row
            bottom_row=max(self.x,board.matrix.shape[1]-1-self.x)              
            #left column
            left_column=board.matrix.shape[1]-1-self.x if self.x>board.div else self.x
        
        else:
            #print('else')
            return []    
        
        # PUT REST HERE
        moves_temp=self.aux_curve_moves(board,top_row,right_column,bottom_row,left_column)
        
        
        square_index=moves_temp.index(board.get_square_from_pos((self.x,self.y)))
        
        end=False
        # RIGHT STRAIGHT
        for i in range(square_index+1,len(moves_temp)):
            square=moves_temp[i]
            if square.occupying_piece.color != 'white':
                end=True
                break
            moves.append(square)
        
        # Reached the end of the list, so we need to check the beginning
        if not end:
            for i in range(0,square_index):
                square=moves_temp[i]
                if square.occupying_piece.color != 'white':
                    break
                moves.append(square)
        
        end=False
        # LEFT STRAIGHT
        for i in range(square_index-1,-1,-1):
            square=moves_temp[i]
            if square.occupying_piece.color != 'white':
                end=True
                break
            moves.append(square)
        
        # Reached the beginning of the list, so we need to check the end
        if not end:
            for i in range(len(moves_temp)-1,square_index,-1):
                square=moves_temp[i]
                if square.occupying_piece.color != 'white':
                    break
                moves.append(square)
        

    
        return moves


    def moves_anticlockwise(self, board):
        moves=[]
        return moves
        
    def get_possible_moves(self, board):
        output = []
        #print(self.x, self.y)
        output.append(self.moves_up_straight(board))
        #print('Output 1')
        #print(output)
        output.append(self.moves_down_straight(board))
        output.append(self.moves_right_straight(board))
        output.append(self.moves_left_straight(board))
        output.append(self.moves_clockwise(board))
        #print(output)
        return output
    
    
    
    def move(self, board, square):
        #print('Entrou na move')
        #print(self.x,self.y)
        for i in board.squares:
            i.highlight = False
        if square in self.get_moves(board):
            prev_square = board.get_square_from_pos(self.pos)
            
            #print("Self x e y")
            #print(self.x, self.y)
            temp=board.matrix[self.y][self.x]
            #print("Temp")
            #print(temp)
            board.matrix[self.y][self.x]=board.matrix[square.y][square.x]
            board.matrix[square.y][square.x]= temp

            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = Ball((prev_square.x, prev_square.y), 'white', board)
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            return True
            
        else:
            board.selected_piece = None
            return False
        
    def experimental_move(self, board, square):
        #print('Entrou na experimental_move')
        #print(self.x,self.y)
        #print(square)
        #newMatrix = copy.deepcopy(board.matrix)
        new_matrix=copy.deepcopy(board.matrix)
        
        
        temp= board.matrix[self.y][self.x]
        new_matrix[self.y][self.x]=new_matrix[square.y][square.x]
        new_matrix[square.y][square.x]= temp
        new_board= board.copy(new_matrix)
        
        
        """ prev_square = new_board.get_square_from_pos(self.pos)
        
        #print("Matrix: ")
        #print(new_board.matrix)
        temp= new_board.matrix[self.y][self.x]
        #print("Temp")
        #print(temp)
        new_board.matrix[self.y][self.x]=new_board.matrix[square.y][square.x]
        new_board.matrix[square.y][square.x]= temp
        
        self.pos, self.x, self.y = square.pos, square.x, square.y
        prev_square.occupying_piece = Ball((prev_square.x, prev_square.y), 'white', new_board)
        square.occupying_piece = self
        new_board.selected_piece = None
        self.has_moved = True """
        #print("Carai, era suposto mudar")
        new_board.turn = 'blue' if board.turn == 'red' else 'red'
        #print(new_board.turn)
        return new_board
            
     

