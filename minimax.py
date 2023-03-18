import pygame
import numpy as np

#Em primeiro lugar, verificar se o estado alcançado vai ser terminal (gameover)

def minimax(board,color, depth, alpha, beta, evaluate, maximizing_player):
    if depth == 0 or board.check_gameover(color):
        #print("In minimax evaluate")
        #print(evaluate(board))
        return evaluate(board)

    if maximizing_player:
        max_flag=0
        max_eval = float('-inf')
        for piece in board.get_pieces():
            for move in piece.occupying_piece.get_moves(board):
                new_board = piece.occupying_piece.experimental_move(board, move)
                #print("welelelele")
                #print(new_board.board)
                eval = minimax(new_board,color,depth - 1,alpha,beta,evaluate,False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha: 
                    max_flag=1
                    break
            if max_flag:
                break
        return max_eval
    else:
        min_eval = float('inf')
        min_flag=0
        for piece in board.get_pieces():
            for move in piece.occupying_piece.get_moves(board):
                new_board = piece.occupying_piece.experimental_move(board, move)
                #print("kkkkkkkkkk")
                #print(new_board.board)
                eval = minimax(new_board,color,depth - 1,alpha,beta,evaluate,True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha: 
                    min_flag=1
                    break
            if min_flag:
                break
        return min_eval
    
    

def execute_minimax_move(evaluate,depth,board):
    print("In execute minimax move")
    print(evaluate(board))
    
    best_move = None
    best_eval=float('-inf')
    best_piece=None
     
    for piece in board.get_pieces():
        for move in piece.occupying_piece.get_moves(board):
            new_board=piece.occupying_piece.experimental_move(board, move)
            new_board_eval=minimax(new_board,board.turn,depth - 1,float('-inf'),float('+inf'),evaluate,False)
            print("New board eval")
            print(new_board_eval)
            if new_board_eval > best_eval:
                print("Onolulo")
                #print(new_board.board)
                #best_move=new_board
                best_piece=piece
                best_move=move
                best_eval=new_board_eval
    
    
    print("Before retunr")
    #board=best_move
    tet_board=best_piece.occupying_piece.experimental_move(board, best_move)
    return tet_board