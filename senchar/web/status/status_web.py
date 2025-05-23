"""
DASH web server for senchar
"""

import logging

from dash import Dash, html, dcc, callback, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import dash_daq as daq

from senchar.web.status.status_card import statusweb_card


class StatusWeb(object):
    """
    Web server using Dash (plotly).
    """

    def __init__(self) -> None:

        self.app = Dash(
            __name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            suppress_callback_exceptions=False,
            requests_pathname_prefix="/status/",
        )
        logging.getLogger("werkzeug").setLevel(logging.CRITICAL)  # stop messages

        self.statusweb_card = statusweb_card()

        # app layout
        self.app.layout = html.Div(
            [
                self.statusweb_card,
                dcc.Interval("statusweb_interval", interval=1_000, n_intervals=0),
            ]
        )

        return
