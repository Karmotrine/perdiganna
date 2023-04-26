from .constants import RED, BLACK, SQUARE_SIZE, GRAY

class Piece:

    # in pixels
    PADDING = 10
    OUTLINE = 2

    def __init___(self, row, col, color):
        self.row = row
        self.col = col
        # Red Piece = Player (Bottom)
        # Black Piece = CPU (Top)
        self.color = color
        self.king = False
        # Positive = Downwards, Negative = Upwards
        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * (self.col + SQUARE_SIZE // 2)
        self.y = SQUARE_SIZE * (self.row + SQUARE_SIZE // 2)

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = (SQUARE_SIZE // 2) - self.PADDING
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

    # Object Debugging
    def __repr__(self):
        return str(self.color)
