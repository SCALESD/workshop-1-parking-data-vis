#!/usr/bin/python

# Plotting map points on Google Maps with interaction
#
# Run: bokeh serve workshop-1.6.py

import json
from gmapplot import GoogleMapPlot
from parking.meter import Meter
from parking.transaction import Transaction

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
assert 'GoogleMapsAPIKey' in config and len(config['GoogleMapsAPIKey']) > 0, "Add your own Google Maps API Key to config.json"
plot = GoogleMapPlot(config['GoogleMapsAPIKey'], SAN_DIEGO_COORDINATE[0], SAN_DIEGO_COORDINATE[1], "roadmap", DEFAULT_ZOOM)


# Load the parking meter transactions before we start
Transaction.transactions()

poles = Meter.poles_in_gaslamp()
draw_xy = [(x.lat, x.long) for x in poles]

datasource = plot.draw_points_with_circle_glyph(draw_xy, { 'fill_color' : 'blue',
							  							   'size' : 3 })



def update_plot(day):
	transactions = set(map(lambda t: t.pole, Transaction.transactions_for_day(day)))
	
	draw_poles = filter(lambda p: p.id in transactions, poles)
	draw_xy = [(x.lat, x.long) for x in draw_poles]
	
	plot.update(datasource, draw_xy)

	# Uncomment to print the selected day of the week to the console
	#import datetime
	#print((datetime.datetime(2017, 1, 1) + datetime.timedelta(day - 1)).strftime('%A'))


plot.add_slider(1, 365, 1, 1, "Day", update_plot)

plot.show()

