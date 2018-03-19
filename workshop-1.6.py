#!/usr/bin/python

# Plotting map points on Google Maps with interaction
#
# Run: bokeh serve workshop-1.6.py

from config import get_config
from constants import DEFAULT_ZOOM, SAN_DIEGO_COORDINATE
from gmapplot import GoogleMapPlot
from parking.meter import Meter
from parking.transaction import Transaction


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

# Load the parking meter transactions before we start
Transaction.transactions()

poles = Meter.poles_in_gaslamp()
draw_xy = [(x.lat, x.lng) for x in poles]

datasource = plot.draw_points_with_circle_glyph(draw_xy, attrs={'fill_color': 'blue', 'size': 3})


def update_plot(day):
    transactions = set([t.pole for t in Transaction.transactions_for_day(day)])

    poles_to_draw = [p for p in poles if p.id in transactions]
    draw_xy = [(pole.lat, pole.lng) for pole in poles_to_draw]

    plot.update(datasource, draw_xy)

    # Uncomment to print the selected day of the week to the console
    # import datetime
    # print((datetime.datetime(2017, 1, 1) + datetime.timedelta(day - 1)).strftime('%A'))

plot.add_slider(start=1, end=365, step=1, init=1, title="Day", callback=update_plot)
update_plot(day=1)  # Slider is initialized to Day 1, make sure plot reflects that

plot.show()
