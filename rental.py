import logging


class Rental:
	"""
	A rental of a movie by customer.
	From Fowler's refactoring example.

	A realistic Rental would have fields for the dates
	that the movie was rented and returned, from which the
	rental period is calculated.
	For simplicity of this application only days_rented is recorded.
	"""

	def __init__(self, movie, days_rented):
		"""Initialize a new movie rental object for
		a movie with known rental period (daysRented).
		"""
		self.movie = movie
		self.days_rented = days_rented

	def get_movie(self):
		return self.movie

	def get_days_rented(self):
		return self.days_rented

	def get_price(self):
		"""compute rental change"""
		return self.movie.get_price(self.days_rented)

	def rental_points(self):
		"""compute the frequent renter points based on movie price code"""
		if self.get_movie().get_price_code() == self.movie.NEW_RELEASE:
			# New release earns 1 point per day rented
			return self.get_days_rented()
		# other rentals get 1 point
		return 1
