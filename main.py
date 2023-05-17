import pygame
from engine.constants import WIDTH, HEIGHT, SQUARE_SIZE
from engine.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Perdigana')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    # Event-time to FPS
    clock = pygame.time.Clock()
    board = Board()
    
    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Piece Move Interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        board.draw(WIN)
        pygame.display.update()

    ##################################################################
    pygame.quit()


main()
