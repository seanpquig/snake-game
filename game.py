from board import Board
from moves import VALID_MOVES


def main():
    board = Board(num_apples=10)

    print('Initial board:')
    print(board)

    game_over = False
    while not game_over:
        move = input()
        if move in VALID_MOVES:
            game_over = board.process_move(move)
            print('\n')
            print(board)

            if game_over:
                print('\nYOU WON!')
        else:
            print(f'Invalid move (must be one of {VALID_MOVES})')


if __name__ == "__main__":
    main()
