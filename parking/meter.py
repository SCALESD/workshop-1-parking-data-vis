#!/usr/bin/python

import csv

from constants import GASLAMP_BOUNDING_BOX, PARKING_METER_LOCATION_DATA_FILE


class Meter:
    def __init__(self, data):
        self.id = data['pole']
        self.lng = float(data['longitude'])
        self.lat = float(data['latitude'])

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
    def poles_in_region(cls, bounding_box):
        lat_a, lng_a, lat_b, lng_b = bounding_box
        return [pole for pole in cls.allpoles() if (pole.lat <= lat_a and
                                                    pole.lat >= lat_b and
                                                    pole.lng >= lng_a and
                                                    pole.lng <= lng_b)]

    @classmethod
    def poles_in_gaslamp(cls):
        return cls.poles_in_region(bounding_box=GASLAMP_BOUNDING_BOX)
