import unittest
import context
import sys

from simulator.constraint import BoundaryConstraint, ObjectConstraint
from simulator.command import *
from simulator.robot import *
from simulator.simulator import *

logging.disable(logging.CRITICAL)

from io import StringIO
class CommandTest(unittest.TestCase):

    def test_valid_bot_position(self):
        simulator = Simulator(5,5)
        simulator.robot.state = State(Point(0,0),FacingDirection.NORTH.value)

        command = LeftCommand(['LEFT'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,0), FacingDirection.WEST.value))

        command = RightCommand(['RIGHT'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,0), FacingDirection.NORTH.value))

        command = MoveCommand(['MOVE'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,1), FacingDirection.NORTH.value))

        command = PlaceCommand(['PLACE',0,0,'NORTH'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,0), FacingDirection.NORTH.value))


        command = PlaceObjectCommand(['PLACE_OBJECT'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,0), FacingDirection.NORTH.value))

        command = MoveCommand(['MOVE'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(0,0), FacingDirection.NORTH.value))

        out = StringIO()
        sys.stdout = out
        command = ReportCommand(['REPORT'])
        command.apply(simulator)
        self.assertTrue(out.getvalue().strip() == '0,0,NORTH')

    def test_invalid_bot_position(self):
        simulator = Simulator(5,5)
        self.assertFalse(simulator.robot.is_ready())

        command = LeftCommand(['LEFT'])
        command.apply(simulator)

        command = LeftCommand(['RIGHT'])
        command.apply(simulator)

        command = LeftCommand(['MOVE'])
        command.apply(simulator)

        command = PlaceCommand(['PLACE', 5,5,'NORTH'])
        command.apply(simulator)
        self.assertFalse(simulator.robot.is_ready())

        command = PlaceObjectCommand(['PLACE_OBJECT'])
        command.apply(simulator)
        self.assertFalse(simulator.robot.is_ready())

        command = PlaceCommand(['PLACE', 4,4,'NORTH'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.is_ready())


        #Test bot cannot move when it's at the boundary
        command = MoveCommand(['MOVE'])
        command.apply(simulator)
        self.assertTrue(simulator.robot.state == State(Point(4,4), FacingDirection.NORTH.value))



if __name__ == '__main__':
    unittest.main()
