#!/usr/bin/python

# Plotting Map Points on Google Maps
#
# Run: python workshop-1.4.py

import csv

from bokeh.io import show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d

from config import get_config
from constants import DEFAULT_ZOOM, PARKING_METER_LOCATION_DATA_FILE, SAN_DIEGO_COORDINATE


# Data Preparation
locations = []
with open(PARKING_METER_LOCATION_DATA_FILE, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    locations = [row for row in reader]

# print(json.dumps(locations, indent=4, sort_keys=True))

locations = [loc for loc in locations if float(loc['latitude']) != 0 and float(loc['longitude']) != 0]

# print(json.dumps(locations, indent=4, sort_keys=True))


data = ColumnDataSource(
    data=dict(
        lat=[float(loc['latitude']) for loc in locations],
        lng=[float(loc['longitude']) for loc in locations]
    )
)


# Plotting Setup

map_options = GMapOptions(lat=SAN_DIEGO_COORDINATE[0],
                          lng=SAN_DIEGO_COORDINATE[1],
                          map_type="roadmap",
                          zoom=DEFAULT_ZOOM)

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


attrs = {
    'x': 'lng',
    'y': 'lat',
    'size': 3,
    'fill_color': 'blue',
    'fill_alpha': 0.8,
    'line_color': None
}

circle = Circle(**attrs)


plot.add_glyph(data, circle)

show(plot)
