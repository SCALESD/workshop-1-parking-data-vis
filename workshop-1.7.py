#!/usr/bin/python

# Plotting heat mapped points on Google Maps with interaction
#
# Run: bokeh serve workshop-1.7.py

import colormap
from itertools import groupby
from math import floor

from config import get_config
from constants import DEFAULT_ZOOM, HEATMAP_GRANULARITY, HEATMAP_SCALING, SAN_DIEGO_COORDINATE
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
color_map = colormap.color_map(HEATMAP_GRANULARITY)

datasources = [plot.draw_points_with_circle_glyph([], attrs={'fill_color': color_map[i], 'size': 4})
               for i in range(HEATMAP_GRANULARITY)]


def update_plot(day):
    transactions = Transaction.transactions_for_day(day)

    poles_by_heat = [[] for i in range(HEATMAP_GRANULARITY)]
    for pole, grouped_transactions in groupby(transactions, lambda t: t.pole):
        hours = sum([t.duration for t in grouped_transactions])
        i = min(
            floor(HEATMAP_SCALING * hours / Transaction.MAX_DURATION * HEATMAP_GRANULARITY),
            HEATMAP_GRANULARITY - 1
        )
        poles_by_heat[i] += [pole]

    for i in range(HEATMAP_GRANULARITY):
        poles_to_draw = [p for p in poles if p.id in poles_by_heat[i]]
        draw_xy = [(x.lat, x.lng) for x in poles_to_draw]
        plot.update(datasources[i], draw_xy)


plot.add_slider(start=1, end=365, step=1, init=1, title="Day", callback=update_plot)
update_plot(day=1)  # Slider is initialized to Day 1, make sure plot reflects that

plot.show()
