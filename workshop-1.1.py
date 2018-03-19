#!/usr/bin/python

# Basic Bokeh
#
# Run: python workshop-1.1.py


from random import randint

from bokeh.io import show
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Circle


data = ColumnDataSource(
    data=dict(
        x=[randint(0, 20) for x in range(10)],
        y=[randint(0, 20) for x in range(10)],
    )
)

attrs = {
    'x': 'x',
    'y': 'y',
    'size': 10,
    'fill_color': 'blue',
    'fill_alpha': 0.8,
    'line_color': None
}

circle = Circle(**attrs)

fig = figure(title="Random X, Y")
fig.add_glyph(data, circle)

show(fig)
