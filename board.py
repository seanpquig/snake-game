import random
from moves import Move
from snake import Snake

SNAKE_LEN = 4
APPLE_CHAR = '@'


class Board:
    size = 0
    num_apples = 0
    apples_eaten = 0

    snake = Snake()

    def __init__(self, size=8, num_apples=10):
        if SNAKE_LEN > size:
            raise Exception('Snake length cannot be longer than board width')

        if num_apples > size ** 2 - SNAKE_LEN:
            raise Exception(f'{num_apples} apples is too many for a {size}x{size} board')

        self.size = size
        self.num_apples = num_apples

        # setup empty board
        self.matrix = [[' ' for _ in range(size)] for _ in range(size)]

        # draw snake on board
        self.draw_snake()

        # randomly allocate apples to board
        self.draw_apples()

    def __str__(self) -> str:
        return '\n'.join([f"| {' | '.join(row)} |" for row in self.matrix])

    def draw_snake(self):
        for char, coords in self.snake.zipped_chars_and_coordinates():
            i, j = coords[0], coords[1]
            self.matrix[i][j] = char

    def draw_apples(self):
        apples_drawn = 0

        while apples_drawn < self.num_apples:
            i, j = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            cell_val = self.matrix[i][j]

            if cell_val == ' ':
                self.matrix[i][j] = APPLE_CHAR
                apples_drawn += 1

    def process_move(self, move: Move):
        if move == Move.LEFT.value and self.snake.head[1] > 0:
            pass
        elif move == Move.RIGHT.value and self.snake.head[1] < self.size - 1:
            pass
        elif move == Move.UP.value and self.snake.head[0] > 0:
            pass
        elif move == Move.DOWN.value and self.snake.head[0] < self.size - 1:
            pass
        else:
            raise Exception('Snake hit wall.  GAME OVER!')

        self.snake.update(move)
        self.snake.info()

        # Return game over status
        return False
