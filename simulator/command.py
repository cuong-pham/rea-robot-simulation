from .direction import *
from .robot import State
from .geometry import Point
from .constraint import ObjectConstraint
import logging

class Command():

    def __init__(self, ast):
        pass

    def apply(self, simulator):
        if not simulator.robot.is_ready():
            logging.info("Bot is not ready")
        pass

    @classmethod
    def name(cls):
        return ""

class LeftCommand(Command):

    def apply(self, simulator):
        robot = simulator.robot
        if robot.is_ready():
            new_facing = robot.state.facing.rotate_90(RotationDirection.LEFT)
            robot.apply(State(robot.state.point, new_facing), simulator.constraints)
        super(LeftCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "LEFT"

class RightCommand(Command):

    def apply(self, simulator):
        robot = simulator.robot
        if robot.is_ready():
            new_facing = robot.state.facing.rotate_90(RotationDirection.RIGHT)
            robot.apply(State(robot.state.point, new_facing), simulator.constraints)
        super(RightCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "RIGHT"

class MoveCommand(Command):

    def apply(self, simulator):
        robot = simulator.robot
        if robot.is_ready():
            new_point = robot.state.point.translate(robot.state.facing)
            robot.apply(State(new_point, robot.state.facing), simulator.constraints)
        super(MoveCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "MOVE"

class ReportCommand(Command):

    def apply(self, simulator):
        robot = simulator.robot
        if robot.is_ready():
            print(robot)
        super(ReportCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "REPORT"

class PlaceCommand(Command):

    def __init__(self, ast):
        self.state = State(Point(ast[1],ast[2]),FacingDirection[ast[3]].value)

    def apply(self, simulator):
        robot = simulator.robot
        robot.apply(self.state,simulator.constraints)
        super(PlaceCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "PLACE"
class InvalidCommand(Command):

    @classmethod
    def name(cls):
        return "INVALID COMMAND"

class PlaceObjectCommand(Command):

    def apply(self, simulator):
        robot = simulator.robot
        if robot.is_ready():
            object_location = robot.state.point.translate(robot.state.facing)
            simulator.add_object(object_location)

        super(PlaceObjectCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "PLACE_OBJECT"

class MapCommand(Command):

    def apply(self, simulator):
        print(simulator)
        super(MapCommand, self).apply(simulator)

    @classmethod
    def name(cls):
        return "MAP"

allowed_commands = [LeftCommand, RightCommand, MoveCommand, ReportCommand, PlaceCommand, PlaceObjectCommand, MapCommand]
