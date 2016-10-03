from .constraint import BoundaryConstraint, ObjectConstraint
from .robot import Robot
from .geometry import Point

class Simulator():

    def __init__(self, width, height):
        self.boundary = BoundaryConstraint(width, height)
        self.constraints = [self.boundary]
        self.objects = []
        self.robot = Robot()

    def add_object(self, point):
        if self.boundary.check(point):
            object_constraint = ObjectConstraint(point)
            self.constraints.append(object_constraint)
            self.objects.append(point)
    def __str__(self):
        ret_str = ""
        for y in reversed(range(0, self.boundary.length_y)):
            for x in range(0, self.boundary.length_x):
                temp_point = Point(x,y)
                if temp_point in self.objects or (self.robot.is_ready() and temp_point == self.robot.state.point):
                    ret_str += 'X'
                else:
                    ret_str += '0'
            ret_str +="\n"

        return ret_str
