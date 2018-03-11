#!/usr/bin/python

import csv
from itertools import groupby
import datetime


PARKING_METER_TRANSACTION_DATA_FILE = "data/treas_parking_payments_2017_datasd-gaslamp.csv"

PRICE_PER_HOUR = 1.25


class Transaction:

	MAX_DURATION = 10  # 8AM - 6PM

	def __init__(self, dict):
		self.pole = dict['pole_id']
		self.amount = float(dict['trans_amt']) / 100
		self.start = dict['trans_start']
		self.expire = dict['meter_expire']
		self.duration = self.amount / PRICE_PER_HOUR

		
	@classmethod
	def transactions(cls):
		if not hasattr(cls, '_transactions'):
			transactions = []
			with open(PARKING_METER_TRANSACTION_DATA_FILE, 'r') as csvfile:
				reader = csv.DictReader(csvfile)
				transactions = [Transaction(row) for row in reader]

			cls._transactions = transactions
			
		return cls._transactions


	@classmethod
	def transactions_for_day(cls, day):
		if not hasattr(cls, '_transactions_day_map'):
			transactions = cls.transactions()
			byDay = groupby(transactions, lambda t: t.start[:10])
			cls._transactions_day_map = dict((k, list(g)) for k, g in byDay)
		
		key = (datetime.datetime(2017, 1, 1) + datetime.timedelta(day - 1)).strftime('%Y-%m-%d')

		return cls._transactions_day_map[key] if key in cls._transactions_day_map else []
		
