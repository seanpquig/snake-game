from board import Move


class Snake:
    tail = (0, 0)
    head = (0, 3)
    body_coordinates = [tail, (0, 1), (0, 2), head]
    body_characters = ['-', '-', '-', '>']

    def __init__(self):
        pass

    def info(self):
        '''Snake data info for debugging purposes.'''
        print(f'Body coordinates: {self.body_coordinates}')
        print(f'Body characters: {self.body_characters}')

    def head_char(self):
        return self.body_characters[-1]

    def zipped_chars_and_coordinates(self):
        return zip(self.body_characters, self.body_coordinates)

    def update(self, move: Move):
        '''
        Update internal snake data based on player move. Adjust tail, head,
        and body coordinates. Adjust body characters based on prior snake
        postion and new direction it's facing.
        '''
        if move == Move.LEFT.value:
            self.head = (self.head[0], self.head[1] - 1)
            head_chars = ['-', '<']
        elif move == Move.RIGHT.value:
            self.head = (self.head[0], self.head[1] + 1)
            head_chars = ['-', '>']
        elif move == Move.UP.value:
            self.head = (self.head[0] - 1, self.head[1])
            head_chars = ['|', '^']
        elif move == Move.DOWN.value:
            self.head = (self.head[0] + 1, self.head[1])
            head_chars = ['|', 'v']

        # move tail one position forward
        self.tail = self.body_coordinates[1]

        self.body_coordinates = self.body_coordinates[1:] + [self.head]
        self.body_characters = self.body_characters[1:-1] + head_chars
