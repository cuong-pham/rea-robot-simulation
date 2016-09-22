
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, translation_vector):
        '''
            Trivial translation of an object using vector
        '''
        x = self.x + translation_vector.x
        y = self.y + translation_vector.y
        return Point(x,y)

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

    def __repr__(self):
        return '{}{}'.format(type(self),self.__dict__)

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

class Vector2D():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def rotate_90(self, direction):
        '''
            Take the approach to rotate a vector using Rotation Matrix
            |cos(x)  -sin(x)| |x|  =  |x_new|
            |sin(x)   cos(x)| |y|     |y_new|
            where is the rotation angle. In this method, the rotation
            angle is either 90 or -90 degree. Hence cos(x) = 0 and
            sin(x) is either -1 or 1
        '''
        if direction != -1 and direction != 1:
            return self

        x = -self.y * direction
        y = self.x * direction
        return Vector2D(x,y)

    def __str__(self):
        return '({},{})'.format(self.x,self.y)

    def __repr__(self):
        return '{}{}'.format(type(self),self.__dict__)
