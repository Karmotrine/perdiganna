import time
from copy import deepcopy
import pygame

from engine.game import Game
from engine.board import Board
from engine.ttable import TTable
from watchpoints import watch

RED = (255,0,0)
BLACK = (0, 0, 0)


class AlphaBetaAgent:
    def __init__(self, move_timeout: float):
        # in seconds?
        self.move_timeout = move_timeout
        # ???
        #self.eval_fn = eval_fn
        self.start_time = 0
        self.cache_table = TTable()
        print("ABP Agent intialized")

    def is_out_of_time(self):
        return time.monotonic() - self.start_time > self.move_timeout

    def prune(self, position: Board, depth: int, alpha: float, beta: float, max_player: tuple, game: Game, activate_timer: bool = True):
        # Iterative Deepening Timer
        if activate_timer and self.is_out_of_time():
            # Match return type
            return 0, 0
        
        # Access Transposition Table Cache
        # What is Board vs Position vs Game? Review Tutorial
        # Dict vs Class as data value?
        
        key_exists = self.cache_table.check_key(position)
        if type(key_exists) == int:
            transposition_cache = self.cache_table.map[self.cache_table.get_hash(position)]
            if transposition_cache.depth >= depth:
                # Shouldn't you return the best_move as well?
                if transposition_cache['flag'] == "EXACT":
                    return transposition_cache['evaluation'], transposition_cache['best_move']
                elif transposition_cache['flag'] == "LOWERBOUND":
                    alpha = max(beta, transposition_cache['evaluation'])
                else: # elif transposition_cache.flag == "UPPERBOUND":
                    beta = min(beta, transposition_cache['evaluation'])
                # What is this for?
                if alpha >= beta:
                    return transposition_cache['evaluation'], transposition_cache['best_move']
            
        # Recursion Base-Case / Terminating Function
        if (depth == 0) or (position.winner() is not None):
            # What datatype is position?
            return position.evaluate(), position
        
        # ABP:
        if max_player == BLACK:
            # Worst-case scenario score
            maxEval = float('-inf')
            # copy of alpha
            best_move = None
            for move in self.get_all_moves(position, BLACK, game):
                current_evaluation = self.prune(position, depth - 1, alpha, beta, RED, game, True)[0] # Complete All Params
                if current_evaluation > maxEval: 
                    best_move = move
                maxEval = max(current_evaluation, maxEval)
                alpha = max(alpha, maxEval)
                # What?
                if maxEval >= beta:
                    break
            thisFlag = "EXACT"
            if maxEval <= beta:
                thisFlag = "UPPERBOUND"
            elif maxEval >= alpha:
                thisFlag = "LOWERBOUND"
            values = {
                'depth': depth, 
                'evaluation': maxEval, 
                'alpha': alpha, 
                'beta': beta,
                'best_move': best_move,
                'flag': thisFlag
            }
            self.cache_table.store_value(position, values)
            return maxEval, best_move
        else:
            # Worst-case scenario score
            minEval = float('inf')
            # Why need copy of alpha/beta?
            best_move = None
            for move in self.get_all_moves(position, RED, game):
                current_evaluation = self.prune(position, depth - 1, alpha, beta, BLACK, game, True)[0] # Complete all params
                if current_evaluation < minEval:
                    best_move = move
                    minEval = min(current_evaluation, minEval)
                beta = min(beta, minEval)
                
                if alpha >= minEval:
                    break
            thisFlag = "EXACT"
            if minEval >= beta:
                thisFlag = "UPPERBOUND"
            elif minEval <= alpha:
                thisFlag = "LOWERBOUND"
            values = {
                'depth': depth, 
                'evaluation': minEval, 
                'alpha': alpha, 
                'beta': beta,
                'best_move': best_move,
                'flag': thisFlag
            }
            self.cache_table.store_value(position, values)
            return minEval, best_move

        
        
    def decide(self, position: Board, max_player, game: Game):
        # Wrapper function to add depth and limit time
        self.start_time = time.monotonic()
        current_depth = 1 # 1 or 0?
        current_best_move = None
        current_maxEval = None

        print("Before starting pruning")
        print(f"{self.is_out_of_time()}")
        while not self.is_out_of_time():
            current_maxEval, current_best_move = self.prune(position, current_depth, float('-inf'), float('inf'), BLACK, game, True)
            current_depth += 1
        
        return current_maxEval, current_best_move

        
    def simulate_move(self, piece, move, board, game, skip):
        board.move(piece, move[0], move[1])
        if skip:
            board.remove(skip)

        return board
                
    def draw_moves(self, game : Game, board : Board, piece):
        valid_moves = board.get_valid_moves(piece)
        board.draw(game.win)
        pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
        game.draw_valid_moves(valid_moves.keys())
        pygame.display.update()
        #pygame.time.delay(100)

    def get_all_moves(self, board : Board, color : tuple, game : Game):
        moves = []

        for piece in board.get_all_pieces(color):
            valid_moves = board.get_valid_moves(piece)
            for move, skip in valid_moves.items():
                self.draw_moves(game, board, piece)
                temp_board = deepcopy(board)
                temp_piece = temp_board.get_piece(piece.row, piece.col)
                new_board = self.simulate_move(temp_piece, move, temp_board, game, skip)
                moves.append(new_board)
        
        return moves


"""
Upperbounds/Lowerbounds
    - https://github.com/looper-m/checkers-ai/blob/master/MTDf.py
    - https://github.com/danthurston/BeatMyChessAI/blob/main/mtdf.py
"""
