#!/usr/bin/python

# Plotting Map Points on Google Maps
#
# Run: bokeh serve workshop-1.5.py

from config import get_config
from constants import DEFAULT_ZOOM, SAN_DIEGO_COORDINATE
from gmapplot import GoogleMapPlot
from parking.meter import Meter

# Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value in config.json below with your personal API key:
config = get_config()
plot = GoogleMapPlot(
    api_key=config['GoogleMapsAPIKey'],
    lat=SAN_DIEGO_COORDINATE[0],
    lng=SAN_DIEGO_COORDINATE[1],
    type="roadmap",
    zoom=DEFAULT_ZOOM
)

poles = Meter.poles_in_gaslamp()
lat_lng_points = [(p.lat, p.lng) for p in poles]

plot.draw_points_with_circle_glyph(lat_lng_points, attrs={'fill_color': 'blue', 'size': 3})

plot.show()
