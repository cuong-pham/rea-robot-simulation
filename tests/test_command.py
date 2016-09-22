import unittest
import context
import sys

from simulator.constraint import BoundaryConstraint
from simulator.command import *
from simulator.robot import *
logging.disable(logging.CRITICAL)

from io import StringIO
class CommandTest(unittest.TestCase):

    def setUp(self):
        self.constraints = BoundaryConstraint(5,5)

    def test_valid_bot_position(self):
        robot = Robot([self.constraints])
        robot.state = State(Point(0,0),FacingDirection.NORTH.value)

        command = LeftCommand(['LEFT'])
        command.apply(robot)
        self.assertTrue(robot.state == State(Point(0,0), FacingDirection.WEST.value))

        command = RightCommand(['RIGHT'])
        command.apply(robot)
        self.assertTrue(robot.state == State(Point(0,0), FacingDirection.NORTH.value))

        command = MoveCommand(['MOVE'])
        command.apply(robot)
        self.assertTrue(robot.state == State(Point(0,1), FacingDirection.NORTH.value))

        command = PlaceCommand(['PLACE',0,0,'NORTH'])
        command.apply(robot)
        self.assertTrue(robot.state == State(Point(0,0), FacingDirection.NORTH.value))

        out = StringIO()
        sys.stdout = out
        command = ReportCommand(['REPORT'])
        command.apply(robot)
        self.assertTrue(out.getvalue().strip() == '0,0,NORTH')

    def test_invalid_bot_position(self):
        robot = Robot([self.constraints])
        self.assertFalse(robot.is_ready())

        command = LeftCommand(['LEFT'])
        command.apply(robot)

        command = LeftCommand(['RIGHT'])
        command.apply(robot)

        command = LeftCommand(['MOVE'])
        command.apply(robot)

        command = PlaceCommand(['PLACE', 5,5,'NORTH'])
        command.apply(robot)
        self.assertFalse(robot.is_ready())

        command = PlaceCommand(['PLACE', 4,4,'NORTH'])
        command.apply(robot)
        self.assertTrue(robot.is_ready())

        #Test bot cannot move when it's at the boundary
        command = MoveCommand(['MOVE'])
        command.apply(robot)
        self.assertTrue(robot.state == State(Point(4,4), FacingDirection.NORTH.value))


if __name__ == '__main__':
    unittest.main()
