"""
file: read_rootfile.py
brief:
usage: python3 read_rootfile.py
note:
author: Oliver LOURGO, olivier.lourgo@iphc.cnrs.fr
"""

from taf_logger import Logger as LOG
from taf_data_handler import get_df_from_rootfile
from argparse import ArgumentParser
from yaml import load as ymlLoad
from yaml import FullLoader as ymlFullLoader
from pprint import pformat


def main(name_config_file: str, debug: bool) -> None:
    """
    Main function

    Args:
        debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")

    config: dict = {}
    with open(name_config_file, "r", encoding="utf-8") as yml_config_file:
        config = ymlLoad(yml_config_file, ymlFullLoader)
    rootfile = config["input"]["file"]
    tree_name = config["input"]["tree"]
    branches_name = config["input"]["branches"]

    df_t = get_df_from_rootfile(rootfile, tree_name, branches_name)
    LOG(df_t.head(3), "RESULT")


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
