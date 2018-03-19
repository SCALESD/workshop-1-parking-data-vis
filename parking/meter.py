#!/usr/bin/python

import csv

PARKING_METER_LOCATION_DATA_FILE = "data/treas_parking_meters_loc_datasd.csv"

GASLAMP_BOUNDING_BOX = (32.716, -117.164, 32.705749, -117.157)


class Meter:

    def __init__(self, dict):
        self.id = dict['pole']
        self.long = float(dict['longitude'])
        self.lat = float(dict['latitude'])

    @classmethod
    def allpoles(cls):
        if not hasattr(cls, '_poles'):
            poles = []

            with open(PARKING_METER_LOCATION_DATA_FILE, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                poles = [Meter(row) for row in reader]

            cls._poles = poles

        return cls._poles

    @classmethod
    def pole_for_location(cls, pole):
        if not hasattr(cls, '_poles_by_location'):
            poles = {x['pole']: x for x in cls.allpoles()}
            cls._poles_by_location = poles

        return cls._poles_by_location[pole] if pole in cls._poles_by_location else None

    @classmethod
    def poles_in_region(cls, bounding_box):
        lat_a, long_a, lat_b, long_b = bounding_box
        return list(filter(lambda l: (l.lat <= lat_a and l.lat >= lat_b and
                                      l.long >= long_a and l.long <= long_b, cls.allpoles())))

    @classmethod
    def poles_in_gaslamp(cls):
        return cls.poles_in_region(bounding_box=GASLAMP_BOUNDING_BOX)
