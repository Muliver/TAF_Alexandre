"""
file: test_debug_switch_argument.py
brief:
usage: python3 test_debug_switch_argument.py
note:
author: Oliver LOURGO, olivier.lourgo@iphc.cnrs.fr
"""

from taf_logger import Logger as LOG
from argparse import ArgumentParser


def main(debug: bool) -> None:
    """
    Main function

    Args:
        debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="program_name.py",
        description="Description of the program",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("-d", "--debug", default=False, action="store_true", help="debug flag")
    args = parser.parse_args()
    main(args.debug)
