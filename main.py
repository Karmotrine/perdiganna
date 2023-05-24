import pygame
from engine.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, BLACK
from engine.board import Board
from engine.game import Game
from engine.agent import AlphaBetaAgent
from engine.algorithm import minimax

from watchpoints import watch

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
    # Make a new Agent object
    # Test for 7 seconds
    this_agent : AlphaBetaAgent = AlphaBetaAgent(7)
    watch(game.board)

    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            #print(f"Start: {game}")
            #value, new_board = minimax(game.get_board(), 4, BLACK, game)
            value, new_board = this_agent.decide(game.get_board(), BLACK, game)
            game.ai_move(new_board)
            #print(f"DD: ${game}")
            
        if game.winner() != False:
            #print(game.winner())
            print("test")
        
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
