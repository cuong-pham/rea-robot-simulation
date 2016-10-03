from .geometry import *
from .direction import *
from .constraint import BoundaryConstraint

class State():
    def __init__(self, point, facing):
        self.point = point
        self.facing = facing

    def is_valid(self, constraints):
        return all([constraint.check(self.point) for constraint in constraints])

    def __repr__(self):
        return '{}{}'.format(type(self),self.__dict__)

    def __eq__(self, other):
        if other is None:
            return False
        return self.point == other.point and self.facing == other.facing

class Robot():

    def __init__(self):
        self.state = None

    def apply(self, state, constraints):
        if state.is_valid(constraints):
            self.state = state

    def __str__(self):
        if self.is_ready():
            return '{},{},{}'.format(
                self.state.point.x, self.state.point.y,
                FacingDirection(self.state.facing).name
            )
        else:
            return ""

    def __repr__(self):
        return '{}{}'.format(type(self),self.__dict__)

    def is_ready(self):
        return self.state != None
