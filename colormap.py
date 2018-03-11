#!/usr/bin/python

import colorsys
    
def color_map(count):
	def rgb_to_hex(red, green, blue):
		return '#{:02X}{:02X}{:02X}'.format(red, green, blue)

	dHue = .33 / float(count - 1)
	colorMap = []
	for i in range(count):
		colorMap += [rgb_to_hex(*map(lambda v: int(255 * v), colorsys.hls_to_rgb(.33 - (dHue * float(i)), .5, 1)))]

	return colorMap