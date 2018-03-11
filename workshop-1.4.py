#!/usr/bin/python

# Plotting Map Points on Google Maps
#
# Run: python workshop-1.4.py

import csv
import json

from bokeh.io import show
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d


PARKING_METER_LOCATION_DATA_FILE = "data/treas_parking_meters_loc_datasd.csv"

SAN_DIEGO_COORDINATE = (32.716, -117.1611)
DEFAULT_ZOOM = 15

# Read the config.json file
config = []
with open('config.json', 'r') as f:
	config = json.load(f)


# Data Preparation
locations = []
with open(PARKING_METER_LOCATION_DATA_FILE, 'r') as csvfile:
	reader = csv.DictReader(csvfile)
	locations = [row for row in reader]
					
#print(json.dumps(locations, indent=4, sort_keys=True))

locations = list(filter(lambda x: float(x['latitude']) != 0 and float(x['longitude']) != 0, locations))

#print(json.dumps(locations, indent=4, sort_keys=True))


data = ColumnDataSource(
	data=dict(
		lat = [float(loc['latitude']) for loc in locations],
		long = [float(loc['longitude']) for loc in locations]
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
assert 'GoogleMapsAPIKey' in config and len(config['GoogleMapsAPIKey']) > 0, "Add your own Google Maps API Key to config.json"
plot = GMapPlot(api_key = config['GoogleMapsAPIKey'],
				x_range = Range1d(), 
				y_range = Range1d(), 
				map_options = map_options,
				width = 1000,
				height = 600,
				toolbar_location = "above")


attrs = { 'x' : 'long',
 		  'y' : 'lat',
		  'size' : 3,
		  'fill_color' : 'blue',
		  'fill_alpha' : 0.8,
		  'line_color' : None }

circle = Circle(**attrs)


plot.add_glyph(data, circle)

show(plot)
