import logging
from movie import Movie
from datetime import datetime
from pricing import ChildrenPrice, RegularPrice, NewRelease


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	For simplicity of this application only days_rented is recorded.
	"""

	def __init__(self, movie, days_rented: int):
		"""Initialize a new movie rental object for
		a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented
		self.price_code = self.get_price_for_movie()

	def get_price_for_movie(self):
		"""Determine the price code of the movie"""
		if self.movie.year == datetime.now().year:
			return NewRelease()
		for genre in self.movie.genre:
			if genre.lower() in ["children", "childrens"]:
				return ChildrenPrice()
		return RegularPrice()

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price_code(self):
		"""getter for the price code"""
		return self.price_code

	def get_price(self):
		"""compute rental change"""
		return self.price_code.get_price(self.days_rented)

	def rental_points(self):
		"""compute the frequent renter points based on movie price code"""
		return self.price_code.get_rental_points(self.days_rented)
