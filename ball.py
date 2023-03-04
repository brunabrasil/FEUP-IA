import pygame

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

        for i in range(board.board.shape[1]-1, self.y,-1):
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
        for y in range(self.y + 1, board.board.shape[1]):
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
        for x in range(self.x + 1, board.board.shape[1]):
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
        for x in range(self.x)[::-1]:
            square = board.get_square_from_pos((x, self.y))
            if square.occupying_piece is not None:
                if square.occupying_piece.color != 'white':
                    return moves
                moves.append(square)
        
        for x in range(board.board.shape[1] - 1, self.x, -1):
            square = board.get_square_from_pos((x, self.y))
            #print(self.x)
            if square.occupying_piece is not None:
                if square.occupying_piece.color != 'white':
                    return moves
                moves.append(square)
                
        return moves
    
    def moves_clockwise(self,board):
        moves=[]
        moves_temp=[]

        #head
        if self.y>=board.board.shape[1]-board.div or self.y<board.div :
            #DO THINGS HERE
            left_column=min(self.y,board.board.shape[1]-1-self.y)
            for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((i,left_column))
                if square.occupying_piece is not None:
                        moves_temp.append(square)    
            
            
            for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((self.y,i))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
            
            right_column=max(self.y,board.board.shape[1]-1-self.y)
            for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((i,right_column))
                if square.occupying_piece is not None:
                        moves_temp.append(square)
                        
                        
            inverted_line=board.board.shape[1]-1-self.y
            for i in range(board.div,2*board.div):
                square=board.get_square_from_pos((inverted_line,i))
                if square.occupying_piece is not None:
                        moves_temp.append(square)

            
        

            
            return moves
        
        # PUT REST HERE
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
        #print(output)
        return output
    
    
    
    def move(self, board, square):
        print('Entrou na move')
        print(self.x,self.y)
        for i in board.squares:
            i.highlight = False
        if square in self.get_moves(board):
            prev_square = board.get_square_from_pos(self.pos)
            self.pos, self.x, self.y = square.pos, square.x, square.y
            prev_square.occupying_piece = Ball((prev_square.x, prev_square.y), 'white', board)
            square.occupying_piece = self
            board.selected_piece = None
            self.has_moved = True
            return True
            
        else:
            board.selected_piece = None
            return False

