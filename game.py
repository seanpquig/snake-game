from board import Board, VALID_MOVES


def main():
    board = Board(num_apples=10)

    print('Initial board:')
    print(board)

    print('Game starting. Good Luck!')

    game_over = False
    while not game_over:
        move = input()
        if move in VALID_MOVES:
            board.process_move(move)
            print('\n')
            print(board)
        else:
            print(f'Invalid move (must be one of {VALID_MOVES})')


if __name__ == "__main__":
    main()
