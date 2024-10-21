from enum import Enum

# Characters representing directional movement around game board
class Move(Enum):
    LEFT = 'a'
    RIGHT = 'd'
    UP = 'w'
    DOWN = 's'

VALID_MOVES = [m.value for m in Move]
