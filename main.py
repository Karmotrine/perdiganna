import pygame
from engine.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from engine.board import Board
from engine.game import Game

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
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # Piece Move Interaction
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()    

    ##################################################################
    pygame.quit()


main()
