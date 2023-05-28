from lru import LRU
from deepdiff import DeepHash


class TTable:
    def __init__(self):
        # 2^16 = 65536 // 2^32 = 4294967296
        self.map = LRU(4294967296)

    def get_hash(self, board: dict) -> str:
        board_hash = DeepHash(board, apply_hash=True)
        hash_number = DeepHash(board)[board]
        return hash_number

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
    def check_key(self, board: dict) -> bool:
        return self.map.has_key(self.get_hash(board))




"""
Resources:
    - https://github.com/looper-m/checkers-ai/blob/master/transposition_cache.py
    - https://github.com/amitdev/lru-dict
"""