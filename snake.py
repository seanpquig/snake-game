class Snake:
    head = (0, 3)
    body_coordinates = [(0, 0), (0, 1), (0, 2), head]
    body_characters = ['-', '-', '-', '>']

    def __init__(self):
        pass

    def zipped_chars_and_coordinates(self):
        return zip(self.body_characters, self.body_coordinates)
