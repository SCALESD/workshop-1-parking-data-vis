#!/usr/bin/python

# Google Maps
#
# Run: python workshop-1.3.py

import json

from bokeh.io import show
from bokeh.models import GMapPlot, GMapOptions, Range1d

SAN_DIEGO_COORDINATE = (32.712, -117.1611)
DEFAULT_ZOOM = 16

# Read the config.json file
config = []
with open('config.json', 'r') as f:
    config = json.load(f)


lat = SAN_DIEGO_COORDINATE[0]
long = SAN_DIEGO_COORDINATE[1]

map_options = GMapOptions(lat=lat, lng=long, map_type="roadmap", zoom=DEFAULT_ZOOM)


# Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value in config.json below with your personal API key:
assert ('GoogleMapsAPIKey' in config and len(config['GoogleMapsAPIKey']) > 0,
        "Add your own Google Maps API Key to config.json")
plot = GMapPlot(api_key=config['GoogleMapsAPIKey'],
                x_range=Range1d(),
                y_range=Range1d(),
                map_options=map_options,
                width=1000,
                height=600,
                toolbar_location="above")

show(plot)
