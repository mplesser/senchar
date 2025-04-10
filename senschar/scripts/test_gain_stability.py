"""
test gain and noise stability
"""

import sys

import senschar


def test_gain_stability(cycles=5):

    for i in range(cycles):
        print(f"Testing cycle: {i + 1}/{cycles}")
        # senschar.db.tools["exposure"].set_roi(-1, -1, 1, 500, 1, 1)
        senschar.db.tools["gain"].find()

    return


if __name__ == "__main__":
    args = sys.argv[1:]
    test_gain_stability(*args)
