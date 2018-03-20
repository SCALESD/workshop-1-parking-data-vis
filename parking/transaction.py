#!/usr/bin/python

import csv
from itertools import groupby
import datetime

from constants import PARKING_METER_TRANSACTION_DATA_FILE, PRICE_PER_HOUR


class Transaction:
    MAX_DURATION = 10  # 8AM - 6PM

    def __init__(self, data):
        self.pole = data['pole_id']
        self.amount = float(data['trans_amt']) / 100
        self.start = data['trans_start']
        self.expire = data['meter_expire']
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
    def transactions_for_day(cls, num_day_of_2017):
        if not hasattr(cls, '_transactions_day_map'):
            transactions = cls.transactions()
            by_day = groupby(transactions, lambda t: t.start[:10])  # First 10 digits are %Y-%m-%d
            cls._transactions_day_map = {date: list(grouped_transactions) for date, grouped_transactions in by_day}

        date = (datetime.datetime(2017, 1, 1) + datetime.timedelta(num_day_of_2017 - 1)).strftime('%Y-%m-%d')

        return cls._transactions_day_map[date] if date in cls._transactions_day_map else []
