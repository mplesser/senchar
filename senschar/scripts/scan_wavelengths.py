"""
Usage: Run scan_wavelengths
"""

import sys

import senschar


def scan_wavelengths():

    et = 15 * 60.0

    senschar.db.parameters.set_par("imagetest", 0)

    for wave in range(800, 1110, 10):

        print("")
        print("Moving to wavelength is %.0f" % float(wave))
        senschar.db.tools["instrument"].set_wavelength(wave)
        print(
            "Current wavelength is %.0f"
            % senschar.db.tools["instrument"].get_wavelength()
        )

        print("Exposing...")
        senschar.db.tools["exposure"].expose(et, "flat", "wavelength scan: %d" % wave)
        print("Finished")

    # reset
    senschar.db.parameters.set_par("imagetest", 1)

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    scan_wavelengths(*args)
