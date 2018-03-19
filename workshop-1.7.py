#!/usr/bin/python

# Plotting heat mapped points on Google Maps with interaction
#
# Run: bokeh serve workshop-1.7.py

import json
import operator
import colormap
from parking.meter import Meter
from parking.transaction import Transaction
from itertools import groupby
from functools import reduce
from math import floor
from gmapplot import GoogleMapPlot


SAN_DIEGO_COORDINATE = (32.712, -117.1611)
DEFAULT_ZOOM = 16

HEATMAP_GRANULARITY = 10
# Scale the data upwards to get better coloration
HEATMAP_SCALING = 3


# Read the config.json file
config = []
with open('config.json', 'r') as f:
    config = json.load(f)


# Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value in config.json below with your personal API key:
assert ('GoogleMapsAPIKey' in config and len(config['GoogleMapsAPIKey']) > 0,
        "Add your own Google Maps API Key to config.json")
plot = GoogleMapPlot(
    config['GoogleMapsAPIKey'],
    SAN_DIEGO_COORDINATE[0],
    SAN_DIEGO_COORDINATE[1],
    "roadmap",
    DEFAULT_ZOOM
)


# Load the parking meter transactions before we start
Transaction.transactions()
poles = Meter.poles_in_gaslamp()
color_map = colormap.color_map(HEATMAP_GRANULARITY)

datasources = [plot.draw_points_with_circle_glyph([], {'fill_color': color_map[i], 'size': 4})
               for i in range(HEATMAP_GRANULARITY)]


def update_plot(day):
    transactions = Transaction.transactions_for_day(day)

    poles_by_heat = [[] for i in range(HEATMAP_GRANULARITY)]
    for k, g in groupby(transactions, lambda t: t.pole):
        hours = reduce(operator.add, map(lambda t: t.duration, g), 0)
        i = min(
            floor(HEATMAP_SCALING * hours / Transaction.MAX_DURATION * HEATMAP_GRANULARITY),
            HEATMAP_GRANULARITY - 1
        )
        poles_by_heat[i] += [k]

    for i in range(HEATMAP_GRANULARITY):
        draw_poles = filter(lambda p: p.id in poles_by_heat[i], poles)
        draw_xy = [(x.lat, x.long) for x in draw_poles]
        plot.update(datasources[i], draw_xy)


plot.add_slider(1, 365, 1, 1, "Day", update_plot)

plot.show()
