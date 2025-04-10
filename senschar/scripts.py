import importlib
import importlib.util
import os

import senschar
import senschar.exceptions


def loadscripts(packages: list) -> None:
    """
    Load scripts into senschar.db.scripts.
    """

    for package in packages:
        pyfiles = []
        spec = importlib.util.find_spec(package)
        if spec is not None:
            folder = spec.submodule_search_locations[0]
        else:
            return

        # bring all .py modules with same function name into namespace
        _, _, filenames = next(os.walk(folder))
        for file1 in filenames:
            if file1.endswith(".py"):
                pyfiles.append(file1[:-3])
        if "__init__" in pyfiles:
            pyfiles.remove("__init__")

        for pfile in pyfiles:
            try:
                mod = importlib.import_module(f"{package}.{pfile}")
                func = getattr(mod, pfile)
                # senschar.db.scripts[pfile] = func
                senschar.db.cli[pfile] = func
            except Exception as e:
                senschar.log(e)
                senschar.exceptions.warning(f"Could not import script {pfile}")

    return
