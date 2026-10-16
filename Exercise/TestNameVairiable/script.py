"""
file: myscript.py
brief: Simple script to show how to define dosctrings
usage: python3 myscript.py
note:
author: Olivier LOURGO, olivier.lourgo@iphc.cnrs.fr
"""

# CMD + / : Commenter une ou plusieurs lignes
# OPT + UP or DOWN : Bouger une ligne
import module
import pandas as pd


def main(debug: bool = False) -> None:
    """
    main function

    Args:
        debug (bool, optional): _description_. Defaults to False.
    """
    if debug:
        print("DEBUG mod activated")
    print("In script.py, __name__: ", __name__)
    a: int = 1  # type hint, because we love c++
    b: float = 3.14
    c: str = "Hello"  # FIXME: Use this variable
    names: list[str] = []
    dfs: list[pd.DataFrame] = []
    res = sum(1.0, b)
    print(res)
    # TODO: add functionality


def sum(x: float | int, y: float) -> float:  # On peut même mettre le type de sortie
    """# Autodocstring extension
    Helper function to perform a sum

    Args:
        x (float): first arg
        y (float): second arc

    Returns:
        float: sum of arg
    """
    return x + y


if __name__ == "__main__":
    DEBUG: bool = True
    main(DEBUG)
