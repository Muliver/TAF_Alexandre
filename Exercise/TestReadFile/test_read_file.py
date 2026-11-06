"""
file: test_read_file.py
brief:
usage: python3 test_read_file.py
note:
author: Oliver LOURGO, olivier.lourgo@iphc.cnrs.fr
"""

from taf_logger import Logger as LOG
import uproot
import pandas as pd
from taf_data_handler import get_df_from_rootfile


def main(debug: bool) -> None:
    """
    Main function

    Args:
        debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")
    rootfile = "data.root"
    tree_name = "tree"
    branches_name = None
    single_branche = "fEdep"
    df_t = get_df_from_rootfile(rootfile, tree_name, branches_name)
    LOG(df_t.head(3), "RESULT")


if __name__ == "__main__":

    DEBUG: bool = False
    main(DEBUG)
