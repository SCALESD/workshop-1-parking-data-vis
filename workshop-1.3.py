#!/usr/bin/python

# Google Maps
#
# Run: python workshop-1.3.py

from bokeh.io import show
from bokeh.models import GMapPlot, GMapOptions, Range1d

from config import get_config
from constants import DEFAULT_ZOOM, SAN_DIEGO_COORDINATE


lat = SAN_DIEGO_COORDINATE[0]
lng = SAN_DIEGO_COORDINATE[1]

map_options = GMapOptions(lat=lat, lng=lng, map_type="roadmap", zoom=DEFAULT_ZOOM)


# Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value in config.json below with your personal API key:
config = get_config()
plot = GMapPlot(api_key=config['GoogleMapsAPIKey'],
                x_range=Range1d(),
                y_range=Range1d(),
                map_options=map_options,
                width=1000,
                height=600,
                toolbar_location="above")

show(plot)
