class Constraint():

    def check(self, state):
        pass

class BoundaryConstraint(Constraint):

    def __init__(self, length_x, length_y):
        self.length_x = length_x
        self.length_y = length_y

    def check(self, point):
        if point.x in range(0,self.length_x) \
                and point.y in range(0,self.length_y):
            return True
        return False
class ObjectConstraint(Constraint):
    def __init__(self, point):
        self.point = point

    def check(self, point):
        if point == self.point:
            return False
        return True
