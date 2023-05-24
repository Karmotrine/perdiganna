"""
Transposition Table
       - Make it LRU Cache (https://github.com/amitdev/lru-dict)
       - Make it store {alpha, beta, evaluation}
       - Make a Zobrist Hashing for Keys
"""
from lru import LRU
from random import getrandbits
from .board import Board

"""
Board Format:
[
	[0, (0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0)], 
	[(0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0), 0], 
	[0, (0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0), 0, (0, 0, 0)], 
	[0, 0, 0, 0, 0, 0, 0, 0], 
	[0, (255, 0, 0), 0, 0, 0, 0, 0, 0], 
	[(255, 0, 0), 0, 0, 0, (255, 0, 0), 0, (255, 0, 0), 0],
	[0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0)],
	[(255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0, (255, 0, 0), 0], 
	[],
]
- Empty grid = int
- Occupied grid = tuple
    - Black = (0,0,0)
    - Red = (255,0,0)
    - Empty = 0

"""

BLACK = (0,0,0)
RED = (255,0,0)
from watchpoints import watch


class TTable:
    def __init__(self):
        # 2^16 = 65536 // 2^32 = 4294967296
        self.map = LRU(4294967296)

        self.EMPTY = 0
        self.RED_PIECE = 1
        self.BLACK_PIECE = 2
        self.RED_KING = 2 #?
        self.BLACK_KING = 3 #?

        self.matrix = []
        # Double check this stuff:
        #   - Is the matrix really a 3D Array?
        for row in range(8):
            zobrist_row = []
            for column in range(8):
                zobrist_column = []
                for piece in range(4):
                    zobrist_column.append(getrandbits(128))
                zobrist_row.append(zobrist_column)
            self.matrix.append(zobrist_row)

    def get_hash(self, board: Board):
        hash_code = 0
        for row in range(8):
            for column in range(8):              
                if type(board) == int:
                    print(f"bad board value: {board}")
                this_piece = board.get_piece(row, column)
                # If empty piece, continue
                if this_piece == 0:
                    continue

                # XOR hash_code with the value from the corresponding grid in self.matrix[currentRow][currentCol][self.RED_PIECE]
                if this_piece.color == RED:
                    hash_code ^= self.matrix[row][column][self.RED_PIECE]
                elif this_piece.color == BLACK:
                    hash_code ^= self.matrix[row][column][self.BLACK_PIECE]
                elif this_piece.color == RED and this_piece.king == True:
                    hash_code ^= self.matrix[row][column][self.RED_KING]
                elif this_piece.color == BLACK and this_piece.king == True:
                    hash_code ^= self.matrix[row][column][self.BLACK_KING]

        return hash_code

    # cache_value = {alpha, beta, evaluation, best_move, depth, flag}
    def store_value(self, board, cache_value):
        self.map[self.get_hash(board)] = cache_value

    def get_value(self, board) -> dict:
        return self.map[self.get_hash(board)]

    def get_size(self):
        return self.map.get_size()
    
    def get_items(self):
        return self.map.items()
    
    # Additional Stuff:
    """
    Try to test what happens if we attempt to get a value
    of a game board that has not been cached yet
    """
    def check_key(self, board: Board):
        return self.map.has_key(self.get_hash(board))




"""
Resources:
    - https://github.com/looper-m/checkers-ai/blob/master/transposition_cache.py
    - https://github.com/amitdev/lru-dict
"""