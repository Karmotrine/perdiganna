from copy import deepcopy
import pygame
import time

# Piece Colors, BLACK = AI, RED = PLAYER
RED = (255,0,0)
BLACK = (0, 0, 0)
# seconds
MAX_TIMEOUT = 60

# Need a Wrapper? for Iterative Deepening?
# Iterative deepening = Increase depth as long as it is within time limit
# @See: https://www.perplexity.ai/search?q=how%20can%20i%20join%20iterative%20deepening%20with%20alpha%20beta%20pruning%20in%20a%20checkers%20ai&copilot=true

def make_move(board):
    id_depth = 1
    best_move = None
    is_timeout = False
    start_time = time.time()

    while True:
        time_delta = time.time() - start_time()
        while time_delta <= MAX_TIMEOUT:
            best_move, score = alpha_beta_search(board, id_depth)
            id_depth += 1
    
    """
        Isn't this somehow process-blocking?
    """

    return best_move


def alpha_beta_search(board, max_depth):
    return alpha_beta_pruning(board, max_depth, float('-inf'), float('+inf'), maximizing_player=True)


def alpha_beta_pruning(position, depth, alpha, beta, max_player, game):
    # Iterative Deepening Time Limit
    # @See: https://www.youtube.com/watch?v=qiq64oIusr0
    # Make this a class?

    
    # Check if gameboard {position/game} is already evaluated
        # Return value from transposition table

    # Recursion Base Case (If we are in a terminal game state)    
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BLACK, game):
            evaluation = alpha_beta_pruning(move, depth-1, alpha, beta, False, game)[0]
            maxEval = max(maxEval, evaluation)
            alpha = max(alpha, evaluation)
            # Minimax replaced by ABP
            if maxEval >= evaluation:
                best_move = move

            if beta <= alpha:
                break
            # Is storing evaluation value to board for debugging? @See: [1], [2]

            # Store Game state data {alpha, beta, evaluation, best move} into Transposition Table
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = alpha_beta_pruning(move, depth-1, alpha, beta, True, game)[0]
            minEval = min(minEval, evaluation)
            # I am confused here, @See: [3], compare with [1] and [2]
            beta = min(minEval, beta)
            # Minimax replaced by ABP
            if minEval <= evaluation:
                best_move = move
            if beta <= alpha:
                break
            # Is storing evaluation value to board for debugging? @See: [1], [2]

            # Store Game state data {alpha, beta, evaluation, best move} into Transposition Table
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
    #pygame.time.delay(100)




# Resources:
"""
  ABP:
- [1] https://github.com/njmarko/alpha-beta-pruning-minmax-checkers/blob/main/alpha-beta-pruning-minmax-checkers/game.py
- [2] https://github.com/dimitrijekaranfilovic/checkers/blob/master/checkers.py
- [3] https://github.com/looper-m/checkers-ai/blob/master/MiniMax.py

  Minimax:
- https://github.com/techwithtim/Python-Checkers-AI/blob/master/minimax/algorithm.py#L21

"""



"""
def ai_agent(board, time_limit):
    id_depth = 1
    best_move = None

    start_time = time.time()
    while True:
        time_delta = time.time() - start_time()
        while time_delta <= MAX_TIMEOUT:
            best_move, score = alpha_beta_search(board, id_depth)
            id_depth += 1

    # Isn't this somehow process-blocking?

    return best_move

"""