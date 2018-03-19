#!/usr/bin/python

from bokeh.layouts import widgetbox, column
from bokeh.models import GMapPlot, GMapOptions, ColumnDataSource, Circle, Range1d
from bokeh.models.widgets import Slider
from bokeh.plotting import curdoc


class GoogleMapPlot:

    def __init__(self, api_key, lat, long, type, zoom):
        map_options = GMapOptions(lat=lat, lng=long, map_type=type, zoom=zoom)

        self.plot = GMapPlot(api_key=api_key,
                             x_range=Range1d(),
                             y_range=Range1d(),
                             map_options=map_options,
                             width=1000,
                             height=600,
                             toolbar_location="above")

        self.layout = column(self.plot)

    def show(self):
        curdoc().add_root(self.layout)

    def draw_points_with_circle_glyph(self, data, attrs):
        data = ColumnDataSource(
            data=dict(
                lat=[x[0] for x in data],
                long=[x[1] for x in data],
            )
        )

        defaults = {
            'x': 'long',
            'y': 'lat',
            'size': 2,
            'fill_color': 'blue',
            'fill_alpha': 0.8,
            'line_color': None
        }
        defaults.update(attrs)

        circle = Circle(**defaults)

        self.plot.add_glyph(data, circle)

        return data

    def update(self, source, data):
        source.data = dict(
            lat=[x[0] for x in data],
            long=[x[1] for x in data],
        )

    def add_slider(self, min, max, step, init, title, callback=None):
        slider = Slider(start=min, end=max, value=init, step=step, title=title)

        slider.on_change('value', self.slider_handler_callback)
        self.slider_callback = callback

        self.layout = column(self.plot, widgetbox(slider))

    def slider_handler_callback(self, attr, old, new):
        if hasattr(self, 'slider_callback') and self.slider_callback is not None:
            self.slider_callback(new)
