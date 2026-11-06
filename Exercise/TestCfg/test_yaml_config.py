"""
file: test_yaml_argument.py
brief:
usage: python3 test_yaml_argument.py
note:
author: Oliver LOURGO, olivier.lourgo@iphc.cnrs.fr
"""

from taf_logger import Logger as LOG
from argparse import ArgumentParser
from yaml import load as ymlLoad
from yaml import FullLoader as ymlFullLoader
from pprint import pformat


def main(name_config_file: str, debug: bool) -> None:
    """
    Main function

    Args:
        name_config_file (str): name of the YAML config file to take into account
        debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")
        LOG(name_config_file, "DEBUG")
    config: dict = {}
    with open(name_config_file, "r", encoding="utf-8") as yml_config_file:
        config = ymlLoad(yml_config_file, ymlFullLoader)
    if debug:
        str_config = pformat(config, indent=2, width=100)
        LOG(f"\n{str_config}", "DEBUG")
    # print(config) # Not beautiful ! pformat is better
    str_config_input = pformat(config["input"], indent=2, width=10)
    # LOG(f"\n{str_config_input}", "DEBUG")
    # LOG(config["info"]["campaign"], "DEBUG")
    # LOG(config["info"]["beam"]["energy"], "DEBUG")
    # LOG(config["info"]["runs"], "DEBUG")
    # LOG(config["input"]["branches"], "DEBUG")  # null in YML is translated into None in python


if __name__ == "__main__":
    parser = ArgumentParser(
        prog="program_name.py",
        description="Description of the program",
        epilog="Text at the bottom of help",
    )
    parser.add_argument("-d", "--debug", default=False, action="store_true", help="debug flag")
    parser.add_argument(
        "name_config_file",
        metavar="name_config_file",
        # default="config.yml" #Doesn't work
        help="YAML configuration file",
    )
    args = parser.parse_args()
    main(args.name_config_file, args.debug)
