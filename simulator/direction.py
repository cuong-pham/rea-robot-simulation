from enum import IntEnum, Enum
from .geometry import Vector2D

class RotationDirection(IntEnum):
    LEFT = 1
    RIGHT = -1

class FacingDirection(Enum):
    WEST = Vector2D(-1,0)
    EAST = Vector2D(1,0)
    NORTH = Vector2D(0,1)
    SOUTH = Vector2D(0,-1)
