from enum import Enum

# Characters representing directional movement around game board
class Move(Enum):
    LEFT = 'a'
    RIGHT = 'd'
    UP = 'w'
    DOWN = 's'

VALID_MOVES = [e.value for e in Move]
