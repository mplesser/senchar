"""
*senschar_console.console* is imported to define console mode, create the senscharconsole parameters dictionary, and define a logger.
"""

import senschar
from senschar.logger import Logger
from senschar.parameters import Parameters
from senschar.database import Database


def setup_console():

    senschar.db = Database()
    senschar.db.parameters = Parameters()
    senschar.db.logger = Logger()
    senschar.log = senschar.db.logger.log  # to allow senschar.log()


# setup_console()
