class Constraint():

    def check(self, state):
        pass

class BoundaryConstraint(Constraint):

    def __init__(self, length_x, length_y):
        self.length_x = length_x
        self.length_y = length_y

    def check(self, state):
        if state.point.x in range(0,self.length_x) \
                and state.point.y in range(0,self.length_y):
            return True
        return False
