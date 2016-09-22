import unittest
import context

from simulator.parser import Parser
from simulator.command import *


class ParserTest(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_invalid_command(self):
        command = self.parser.parse_command("Jibberish Command")
        self.assertTrue(isinstance(command, InvalidCommand))

        command = self.parser.parse_command("PLACE 1,2 NORTH") #malform place command
        self.assertTrue(isinstance(command, InvalidCommand))

    def test_valid_command(self):
        command = self.parser.parse_command("LEFT")
        self.assertTrue(isinstance(command, LeftCommand))

        command = self.parser.parse_command("RIGHT")
        self.assertTrue(isinstance(command, RightCommand))

        command = self.parser.parse_command("MOVE")
        self.assertTrue(isinstance(command, MoveCommand))

        command = self.parser.parse_command("REPORT")
        self.assertTrue(isinstance(command, ReportCommand))

        command = self.parser.parse_command("PLACE 1,2,NORTH")
        self.assertTrue(isinstance(command, PlaceCommand))

if __name__ == '__main__':
    unittest.main()
