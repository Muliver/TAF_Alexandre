"""
file: test_logger.py
brief:
usage: python3 test_logger.py
note:
author: Alexandre BIGOT, alexandre.bigot@iphc.cnrs.fr
"""

from taf_logger import Logger as LOG


def main(debug: bool) -> None:
    """
    Main function
    Args:
    debug (bool): Switch for debugging
    """
    if debug:
        LOG("Debug mode activated!", "DEBUG")
        LOG("Petit résultat", "RESULT")
        LOG("Petit Log", "INFO")
        LOG("Petit Warning", "WARNING")
        LOG("Petite Erreur", "ERROR")
        LOG("GROSSE FATAL", "FATAL")
    print("Bonjour")


if __name__ == "__main__":
    DEBUG: bool = True
    main(DEBUG)
