from simulator.parser import Parser
from simulator.robot import Robot
from simulator.simulator import Simulator
from simulator.constraint import BoundaryConstraint
import argparse
import sys, logging

def main(args):
    parser = argparse.ArgumentParser("Robot Challenge CLI")

    parser.add_argument("-v", dest="verbosity", default=0, action="count",
                        help="Increase verbosity. High verbosity is debug mode")

    parser.add_argument("--input", dest="input_file", type=argparse.FileType("r"),
                        default=sys.stdin,
                        help="Input file with series of commands. \
                              If not specified, script will run in interactive mode via stdin")

    parser.add_argument("--width", dest="width", default=5, type=int,
                        help="Width of the grid, default is 5")

    parser.add_argument("--height", dest="height", default=5, type=int,
                        help="Height of the gride, default is 5")

    options = parser.parse_args(args)

    log_level = logging.ERROR
    if options.verbosity == 1:
        log_level = logging.WARNING
    elif options.verbosity == 2:
        log_level = logging.INFO
    elif options.verbosity >= 3:
        log_level = logging.DEBUG


    logging.basicConfig(level=log_level)

    simulator = Simulator(options.width, options.height)

    p = Parser()

    for line in options.input_file:
        command = p.parse_command(line)
        logging.info("Trying to apply command {}".format(command.name()))
        command.apply(simulator)
        logging.debug("Current state of the robot {}".format(simulator.robot))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
