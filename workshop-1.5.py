#!/usr/bin/python

# Plotting Map Points on Google Maps
#
# Run: bokeh serve workshop-1.5.py

import json
from gmapplot import GoogleMapPlot
from parking.meter import Meter

SAN_DIEGO_COORDINATE = (32.712, -117.1611)
DEFAULT_ZOOM = 16

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

poles = Meter.poles_in_gaslamp()

drawnXY = [(x.lat, x.long) for x in poles]

plot.draw_points_with_circle_glyph(drawnXY, {'fill_color': 'blue', 'size': 3})

plot.show()
