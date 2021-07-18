
from typing import List
import datetime


class Round:
	"""bla"""
	number_of_rounds = 1

	def __init__(self, name):
		self.name = name
		self.list_match = []
		self.start_date = datetime.datetime.now()
		self.end_date = ""

		Round.number_of_rounds += 1

	def add_match(self, match):
		self.list_match.append(match)

	def save_date(self):
		self.start_date = datetime.datetime.now()


class Match:
	"""bla"""
	def __init__(self):
		self.mane = ()


