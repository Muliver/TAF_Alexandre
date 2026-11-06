from taf_logger import Logger as LOG

try:
    import uproot
except ModuleNotFoundError:
    print("Module 'uproot' is not installed. Please install it to run this script.")

try:
    import pandas as pd
except ModuleNotFoundError:
    print("Module 'pandas' is not installed. Please install it to run this script.")


def get_df_from_rootfile(
    rootfile_: str, ttree_: str, branches_: None | list[str] | str
) -> pd.DataFrame | list[pd.DataFrame]:
    """
    To generate a panda dataframe from a root file given the mna

    Args:
        RootFile_ (str): name of the rootfile
        Ttree_ (str): name of the tree
        branches_ (str): list of branches, None for all

    Returns:
        pd.DataFrame: _description_
    """
    if not isinstance(ttree_, list):
        return uproot.open(rootfile_)[ttree_].arrays(branches_, library="pd")

    if isinstance(branches_, list):
        if not isinstance(branches_[0], list):
            LOG("name_branches should be a list of list, as name_trees is a list!", "FATAL")

    with uproot.open(rootfile_) as file:
        # get the TTree
        dfs: list[pd.DataFrame] = []
        for ttree_, branches_ in zip(ttree_, ttree_):
            tree: uproot.TTree = file[ttree_]
            arrays = tree.arrays(branches_, library="np")
            dfs.append(pd.DataFrame(arrays))
    return dfs
    # get pandas dataframe from TTree
