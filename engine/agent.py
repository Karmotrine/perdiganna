import time
from copy import deepcopy
import pygame
import ttable

RED = (255,0,0)
BLACK = (0, 0, 0)


class AlphaBetaAgent:
    def __init__(self, move_timeout: float, eval_fn):
        self.move_timeout = move_timeout
        self.eval_fn = eval_fn
        self.start_time = 0
        self.cache_table = ttable()

    def is_out_of_time(self):
        return time.monotonic() - self.start_time > self.move_timeout

    def prune(self, position, board, depth: int, alpha: float, beta: float, max_player: bool, game, activate_timer: bool = True):
        # Iterative Deepening Timer
        if activate_timer and self.is_out_of_time():
            # Match return type
            return 0, 0
        
        # Access Transposition Table Cache
        # What is Board vs Position vs Game? Review Tutorial
        transposition_cache = self.cache_table[self.cache_table.get_hash(board)]
        if transposition_cache is not None and transposition_cache.depth >= depth:
            # Shouldn't you return the best_move as well?
            if transposition_cache.flag == "EXACT":
                return transposition_cache.evaluation, transposition_cache.best_move
            elif transposition_cache.flag == "LOWERBOUND":
                alpha = max(beta, transposition_cache.evaluation)
            elif transposition_cache.flag == "UPPERBOUND":
                beta = min(beta, transposition_cache.evaluation)
            # What is this for?
            if alpha >= beta:
                return transposition_cache.evaluation, transposition_cache.best_move
            
        # Recursion Base-Case / Terminating Function
        if (depth == 0) or (position.winner() is not None):
            # What datatype is position?
            return position.evaluate(), position
        
        # ABP:
        if max_player:
            # Worst-case scenario score
            maxEval = float('-inf')
            best_move = None
            for move in self.get_all_moves(position, BLACK, game):
                current_evaluation = self.prune() # Complete All Params
                maxEval = max(current_evaluation, maxEval)
                alpha = max(alpha, maxEval)
                # How about best_move?
                best_move = move
                if beta <= alpha:
                    break

            # DEBATABLE: A/B values vs Upper/Lower Bound Flags
            thisFlag = "EXACT"
            if maxEval <= beta:
                thisFlag = "UPPERBOUND"
            elif maxEval >= alpha:
                thisFlag = "LOWERBOUND"
            # Check if alpha > maxEval < beta?

            # Store in transposition table
            self.transpositon_table[self.transposition_table.get_hash(board)] = {
                'depth': depth, 
                'evaluation': maxEval, 
                'alpha': alpha, 
                'beta': beta,
                'best_move': best_move,
                'flag': thisFlag
            }

            return maxEval, best_move
                    
        else:
            # Worst-case scenario score
            maxEval = float('inf')
            best_move = None
            for move in self.get_all_moves(position, RED, game):
                current_evaluation = self.prune() # Complete all params
                maxEval = min(current_evaluation, maxEval)
                beta = min(alpha, maxEval)
                # How about best_move?
                best_move = move
                if beta <= alpha:
                    break

            # DEBATABLE: A/B values vs Upper/Lower Bound Flags
            thisFlag = "EXACT"
            if maxEval <= beta:
                thisFlag = "UPPERBOUND"
            elif maxEval >= alpha:
                thisFlag = "LOWERBOUND"
            # Check if alpha > maxEval < beta?

            # Store in transposition table
            self.transpositon_table[self.transposition_table.get_hash(board)] = {
                'depth': depth, 
                'evaluation': maxEval, 
                'alpha': alpha, 
                'beta': beta,
                'best_move': best_move,
                'flag': thisFlag
            }

            return maxEval, best_move
        
    def decide(self, board, ):
        # Wrapper function to add depth and limit time
        self.start_time = time.monotonic()
        current_depth = 1 # 1 or 0?
        current_best_move = None
        current_maxEval = None

        while self.is_out_of_time():
            current_maxEval, current_best_move = None # Turn this into alpha-beta
            current_depth += 1
        
        return current_maxEval, current_best_move

        
    def simulate_move(piece, move, board, game, skip):
        board.move(piece, move[0], move[1])
        if skip:
            board.remove(skip)

        return board
                
    def draw_moves(game, board, piece):
        valid_moves = board.get_valid_moves(piece)
        board.draw(game.win)
        pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
        game.draw_valid_moves(valid_moves.keys())
        pygame.display.update()
        #pygame.time.delay(100)

    def get_all_moves(self, board, color, game):
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
