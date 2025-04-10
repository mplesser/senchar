"""
# shortcuts.py

CLI shortcuts for senschar-console.
"""

import senschar
import senschar.utils


def bf():
    """Shortcut for file_browser()."""

    folder = senschar.utils.file_browser("", "folder", "Select folder")
    if folder == []:
        return
    if isinstance(folder, list):
        folder = folder[0]
    senschar.utils.curdir(folder)

    return folder


def sav():
    """Shortcut for parfile_write() saving current folder in database."""

    senschar.db.parameters.set_par("senscharconsole", "wd", senschar.utils.curdir())
    senschar.db.parameters.update_par_dict()
    senschar.db.parameters.write_parfile()

    return


def sroi():
    """Shortcut for set_image_roi()."""
    senschar.utils.set_image_roi()


# add to cli
senschar.db.cli.update({"sav": sav, "sroi": sroi, "bf": bf})
