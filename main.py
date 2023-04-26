import pygame
from engine.constants import WIDTH, HEIGHT
from engine.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Perdigana')


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
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    ##################################################################
    pygame.quit()


main()
