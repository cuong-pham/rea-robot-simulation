from .direction import *
from .robot import State
from .geometry import Point
import logging

class Command():

    def __init__(self, ast):
        pass

    def apply(self, robot):
        if not robot.is_ready():
            logging.info("Bot is not ready")
        pass

    @classmethod
    def name(cls):
        return ""

class LeftCommand(Command):

    def apply(self, robot):
        if robot.is_ready():
            new_facing = robot.state.facing.rotate_90(RotationDirection.LEFT)
            robot.apply(State(robot.state.point, new_facing))
        super(LeftCommand, self).apply(robot)

    @classmethod
    def name(cls):
        return "LEFT"

class RightCommand(Command):

    def apply(self, robot):
        if robot.is_ready():
            new_facing = robot.state.facing.rotate_90(RotationDirection.RIGHT)
            robot.apply(State(robot.state.point, new_facing))
        super(RightCommand, self).apply(robot)

    @classmethod
    def name(cls):
        return "RIGHT"

class MoveCommand(Command):

    def apply(self, robot):
        if robot.is_ready():
            new_point = robot.state.point.translate(robot.state.facing)
            robot.apply(State(new_point, robot.state.facing))
        super(MoveCommand, self).apply(robot)

    @classmethod
    def name(cls):
        return "MOVE"

class ReportCommand(Command):

    def apply(self, robot):
        if robot.is_ready():
            print(robot)
        super(ReportCommand, self).apply(robot)

    @classmethod
    def name(cls):
        return "REPORT"

class PlaceCommand(Command):

    def __init__(self, ast):
        self.state = State(Point(ast[1],ast[2]),FacingDirection[ast[3]].value)

    def apply(self, robot):
        robot.apply(self.state)
        super(PlaceCommand, self).apply(robot)

    @classmethod
    def name(cls):
        return "PLACE"
class InvalidCommand(Command):

    @classmethod
    def name(cls):
        return "INVALID COMMAND"

allowed_commands = [LeftCommand, RightCommand, MoveCommand, ReportCommand, PlaceCommand]
