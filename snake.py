from board import Move


class Snake:
    head = (0, 3)
    body_coordinates = [(0, 0), (0, 1), (0, 2), head]
    body_characters = ['-', '-', '-', '>']

    def __init__(self):
        pass

    def info(self):
        print(f'Body coordinates: {self.body_coordinates}')
        print(f'Body characters: {self.body_characters}')

    def zipped_chars_and_coordinates(self):
        return zip(self.body_characters, self.body_coordinates)

    def update(self, move: Move):
        last_2_chars = self.body_characters[-2:]

        if move == Move.LEFT.value:
            self.head = (self.head[0], self.head[1] - 1)
            last_2_chars = ['-', '<']
        elif move == Move.RIGHT.value:
            self.head = (self.head[0], self.head[1] + 1)
            last_2_chars = ['-', '>']
        elif move == Move.UP.value:
            self.head = (self.head[0] - 1, self.head[1])
            last_2_chars = ['|', '^']
        elif move == Move.DOWN.value:
            self.head = (self.head[0] + 1, self.head[1])
            last_2_chars = ['|', 'v']

        self.body_coordinates = self.body_coordinates[1:] + [self.head]
        self.body_characters = self.body_characters[1:-1] + last_2_chars
