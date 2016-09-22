import unittest
import context

from simulator.geometry import *
from simulator.direction import *

class GeoTest(unittest.TestCase):

    def test_rotate_90(self):
        vector = FacingDirection.NORTH.value

        east_vector = vector.rotate_90(RotationDirection.RIGHT)
        self.assertTrue(east_vector == FacingDirection.EAST.value)

        west_vector = vector.rotate_90(RotationDirection.LEFT)
        self.assertTrue(west_vector == FacingDirection.WEST.value)

        vector = FacingDirection.SOUTH.value

        east_vector = vector.rotate_90(RotationDirection.LEFT)
        self.assertTrue(east_vector == FacingDirection.EAST.value)

        west_vector = vector.rotate_90(RotationDirection.RIGHT)
        self.assertTrue(west_vector == FacingDirection.WEST.value)

        self.assertTrue(
            west_vector.rotate_90(RotationDirection.RIGHT) ==
                FacingDirection.NORTH.value
        )

        self.assertTrue(
            west_vector.rotate_90(RotationDirection.LEFT) ==
                FacingDirection.SOUTH.value
        )


    def test_translate(self):

        point = Point(1,0)

        self.assertTrue(Point(3,0) == point.translate(Vector2D(2,0)))
        self.assertTrue(Point(2,1) == point.translate(Vector2D(1,1)))

if __name__ == '__main__':
    unittest.main()
