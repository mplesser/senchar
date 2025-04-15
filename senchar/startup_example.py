"""
Startup example for senchar.

Usage example:
  ipython --ipython-dir=/data/ipython --profile senchar -i -m senchar.startup_example
"""

import os

from senchar.tools import *
from senchar import db

from senchar.parameters import Parameters

db.datafolder = "/data"

# values
db.imageroi = [[100, 200, 100, 200]]

# parameters
params = Parameters()
parfile = os.path.join(db.datafolder, "parameters", "senchar.ini")
params.read_parfile(parfile)
params.update_pars()


# shortcuts
def sav():
    params.update_par_dict()
    params.save_pars()
    return
