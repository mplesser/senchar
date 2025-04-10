"""
Scientific image sensor characterization package.
"""

import typing
from typing import List, Dict
from importlib import metadata

__version__ = metadata.version(__package__)
__version_info__ = tuple(int(i) for i in __version__.split(".") if i.isdigit())

from senschar.logger import Logger

from senschar.database import Database

# logger object
logger: Logger = Logger()

# initially senschar.log() is print() but will usually be overwritten
log: typing.Callable = print

# initial database but will ususally be overwritten by server or console
db: Database = Database()

# cleanup namespace
del metadata
del typing
del Logger
del Database
# del database
