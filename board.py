import random
from moves import Move
from snake import Snake

SNAKE_LEN = 4
EMPTY_CHAR = ' '
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
        self.matrix = [[EMPTY_CHAR for _ in range(size)] for _ in range(size)]

        # draw snake on board
        self.draw_snake()

        # randomly allocate apples to board
        self.draw_apples()

    def __str__(self) -> str:
        '''Custom print method for redndering board state in terminal.'''
        row_border = ' - '.join(['+'] * (self.size + 1))
        print_rows = [row_border]

        for row in self.matrix:
            print_rows.append(f"| {' | '.join(row)} |")
            print_rows.append(row_border)

        return '\n'.join(print_rows)

    def draw_snake(self):
        for char, coords in self.snake.zipped_chars_and_coordinates():
            i, j = coords[0], coords[1]
            self.matrix[i][j] = char

    def draw_apples(self):
        apples_placed = 0

        while apples_placed < self.num_apples:
            i, j = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            cell_val = self.matrix[i][j]

            if cell_val == EMPTY_CHAR:
                self.matrix[i][j] = APPLE_CHAR
                apples_placed += 1

    def process_move(self, move: Move):
        '''
        Process a desired game move:
            - check if it causes the snake to hit the wall
            - check if snake can move in direction based on its' current orientation
            - check if snake eats an apple on the board
            - update the snake's positon coordinates and body characters
            - re-draw the snake on the board matrix

        Return boolean idicating if game is over or should continue.
        '''
        snake_head_char = self.snake.head_char()

        # Check if move is valid
        if move == Move.LEFT.value and self.snake.head[1] > 0:
            if snake_head_char == '>':
                print("Snake can't move backwards!")
                return False
        elif move == Move.RIGHT.value and self.snake.head[1] < self.size - 1:
            if snake_head_char == '<':
                print("Snake can't move backwards!")
                return False
        elif move == Move.UP.value and self.snake.head[0] > 0:
            if snake_head_char == 'v':
                print("Snake can't move backwards!")
                return False
        elif move == Move.DOWN.value and self.snake.head[0] < self.size - 1:
            if snake_head_char == '^':
                print("Snake can't move backwards!")
                return False
        else:
            raise Exception('Snake hit wall.  GAME OVER!')

        # Clear prior snake tail position
        tail_i, tail_j = self.snake.tail
        self.matrix[tail_i][tail_j] = EMPTY_CHAR

        # Update snake data based on move
        self.snake.update(move)

        # Check if an apple is eaten
        head_i, head_j = self.snake.head
        if self.matrix[head_i][head_j] == APPLE_CHAR:
            self.apples_eaten += 1
            self.num_apples -= 1
            print(f'Apple eaten! (Total: {self.apples_eaten}, Remaining: {self.num_apples})')

        # Re-draw snake on board
        self.draw_snake()

        # Return game over status
        return self.num_apples == 0
