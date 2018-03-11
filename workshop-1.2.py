#!/usr/bin/python

# CSV Data
#
# Run: python workshop-1.2.py

import csv

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Circle

SAMPLE_XY_FILE = 'data/random-xy.csv'


csvdata = []
with open(SAMPLE_XY_FILE, 'r') as csvfile:
	reader = csv.reader(csvfile)
	csvdata = [row for row in reader]


# Visualize data as json structure
import json
print(json.dumps(csvdata, indent=4, sort_keys=True))


data = ColumnDataSource(
	data=dict(
		x = [int(x[0]) for x in csvdata],
		y = [int(y[1]) for y in csvdata]
	)
)

attrs = { 'x' : 'x',
 		  'y' : 'y',
		  'size' : 10,
		  'fill_color' : 'blue',
		  'fill_alpha' : 0.8,
		  'line_color' : None }

circle = Circle(**attrs)

fig = figure(title = "Random X, Y")
fig.add_glyph(data, circle)

show(fig)
