"""
Used to bring commands into the current namespace.

Usage:  `from senschar.cli import *`

items in `db.cli` are
added to __all__ here for import into the CLI namespace.
"""

import senschar

# main database object
db = senschar.db

# directly put tools in namespace to be imported with *
try:
    for name in senschar.db.cli:
        globals()[name] = senschar.db.cli[name]

    __all__ = [x for x in senschar.db.cli]
except Exception:
    pass

__all__.append("db")
