import pygame
from .constants import WHITE, GREEN, ROWS, SQUARE_SIZE

class Board:
    def __init__(self,):
        # 2D Representation of the Pieces
        self.board = [[]]
        self.selected_piece = None
        self.red_left = self.black_left = 12
        self.red_kings = self.black_kings = 0

    # GREEN, WHITE FOR TILES
    def draw_squares(self, win):
        win.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, GREEN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        pass
