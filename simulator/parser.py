from pyparsing import Word, nums, Literal, Or, ParseException
import logging

class Parser():

    facing_directions = ['NORTH','SOUTH','EAST','WEST']
    simple_commands = ['LEFT','RIGHT','MOVE','REPORT','PLACE_OBJECT','MAP']

    digit = Word(nums).setParseAction(lambda x: int(x[0]))
    facing = Or([Literal(facing) for facing in facing_directions])

    place_command = Literal('PLACE') + digit + Literal(',').suppress() + digit + \
                    Literal(',').suppress() + facing

    command = Or([Literal(simple_command) for simple_command in simple_commands]) \
            | place_command

    def parse_command(self, command_string):
        from .command import allowed_commands, Command, InvalidCommand
        try:
            result = self.command.parseString(command_string)
            for command in allowed_commands:
                if command.name() == result[0]:
                    logging.info("Parse command {}".format(result))
                    return command(result)
        except ParseException:
            logging.warning("Invalid command")
            return InvalidCommand(None)
