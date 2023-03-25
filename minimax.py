import pygame
import numpy as np
import time
#Em primeiro lugar, verificar se o estado alcançado vai ser terminal (gameover)

def minimaxNormal(board,color,depth,evaluate,maximizing_player):
    if depth == 0 or board.check_gameover(color):
        if board.check_gameover(color):
            return 99999999
        return evaluate(board)
    
    if maximizing_player:
        max_eval = float('-inf')
        for piece in board.get_pieces():
            for move in piece.occupying_piece.get_moves(board):
                new_board = piece.occupying_piece.experimental_move(board,move)
                eval = minimaxNormal(new_board,color,depth - 1,evaluate,False)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for piece in board.get_pieces():
            for move in piece.occupying_piece.get_moves(board):
                new_board = piece.occupying_piece.experimental_move(board,move)
                eval = minimaxNormal(new_board,color,depth - 1,evaluate,True)
                min_eval = min(min_eval, eval)
        return min_eval
    

def minimaxAlphaBeta(board,color, depth, alpha, beta, evaluate, maximizing_player):
    if depth == 0 or board.check_gameover(color):
        if board.check_gameover(color):
            return 99999999
        #print("In minimaxAlphaBeta evaluate")
        #print(evaluate(board))
        return evaluate(board)

    if maximizing_player:
        max_flag=0
        max_eval = float('-inf')
        for piece in board.get_pieces():
            for move in piece.occupying_piece.get_moves(board):
                new_board = piece.occupying_piece.experimental_move(board,move)
                #print("welelelele")
                #print(new_board.matrix)
                eval = minimaxAlphaBeta(new_board,color,depth - 1,alpha,beta,evaluate,False)
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
                #new_board = piece.occupying_piece.experimental_move(board, move)
                new_board = piece.occupying_piece.experimental_move(board,move)
                #print("welelelele")
                #print(new_board.matrix)
                #print("kkkkkkkkkk")
                #print(new_board.matrix)
                eval = minimaxAlphaBeta(new_board,color,depth - 1,alpha,beta,evaluate,True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha: 
                    min_flag=1
                    break
            if min_flag:
                break
        return min_eval
    
    

def execute_minimaxAlphaBeta_move(evaluate,depth,board):
    print("In execute minimaxAlphaBeta move")
    #print(board.matrix)
    
    best_move = None
    best_eval=float('-inf')
    best_piece=None
    start = time.time()
    for piece in board.get_pieces():
        for move in piece.occupying_piece.get_moves(board):
            new_board=piece.occupying_piece.experimental_move(board, move)
            new_board_eval=minimaxAlphaBeta(new_board,new_board.turn,depth,float('-inf'),float('+inf'),evaluate,False)
            #print("New board eval")
            #print(new_board_eval)       
            if new_board_eval > best_eval:
                #print("Onolulo")
                #print(new_board.matrix)
                #best_move=new_board
                best_piece=piece
                best_move=move
                best_eval=new_board_eval
    
    end = time.time()
    print("time time taken to get move: ", end-start)
    #print("BEST EVAL:",best_eval)
    #print("Before return")
    #board=best_move
    tet_board=best_piece.occupying_piece.experimental_move(board,best_move)
    #print(tet_board.matrix)
    return tet_board


def execute_minimaxNormal_move(evaluate,depth,board):
    print("In execute minimaxNormal move")
    #print(board.matrix)
    
    best_move = None
    best_eval=float('-inf')
    best_piece=None
    start = time.time()
    for piece in board.get_pieces():
        for move in piece.occupying_piece.get_moves(board):
            new_board=piece.occupying_piece.experimental_move(board, move)
            new_board_eval=minimaxNormal(new_board,new_board.turn,depth,evaluate,False)
            #print("New board eval")
            #print(new_board_eval)       
            if new_board_eval > best_eval:
                #print("Onolulo")
                #print(new_board.matrix)
                #best_move=new_board
                best_piece=piece
                best_move=move
                best_eval=new_board_eval
    
    end = time.time()
    print("time taken to get move: ", end-start)
    #print("BEST EVAL:",best_eval)
    #print("Before return")
    #board=best_move
    tet_board=best_piece.occupying_piece.experimental_move(board,best_move)
    #print(tet_board.matrix)
    return tet_board
