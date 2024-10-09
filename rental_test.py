import unittest
from customer import Customer
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", Movie.NEW_RELEASE)
		self.regular_movie = Movie("Air", Movie.REGULAR)
		self.childrens_movie = Movie("Frozen", Movie.CHILDRENS)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", Movie.REGULAR)
		self.assertEqual("Air", m.get_title())
		self.assertEqual(Movie.REGULAR, m.get_price_code())

	def test_rental_price(self):
		"""Test the price for different kinds of movies"""
		# test new movies
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		# test regular movies
		rental = Rental(self.regular_movie, 2)
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5)
		self.assertEqual(rental.get_price(), 6.5)
		# test children movies
		rental = Rental(self.childrens_movie, 2)
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5)
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		"""Test the rental point gain for different movie types"""
		# test children movies
		rental = Rental(self.childrens_movie, 1)
		self.assertEqual(rental.rental_points(), 1)
		# die hard frozen fans still only get 1 point per rental
		rental = Rental(self.childrens_movie, 99)
		self.assertEqual(rental.rental_points(), 1)
		# test regular movies
		rental = Rental(self.regular_movie, 1)
		self.assertEqual(rental.rental_points(), 1)
		# still only 1 point per rental
		rental = Rental(self.regular_movie, 420)
		self.assertEqual(rental.rental_points(), 1)
		# test new movies
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.rental_points(), 1)
		# new movies get more points per day rented
		rental = Rental(self.new_movie, 50)
		self.assertEqual(rental.rental_points(), 50)

	def test_movies(self):
		"""
		Movies should be different objects but have the same PriceStrategy
		if their types are the same.
		"""
		newer_movie = Movie("The minecraft movie", Movie.NEW_RELEASE)
		self.assertNotEqual(newer_movie, self.new_movie)
		self.assertEqual(newer_movie.price_code, self.new_movie.price_code)
		self.assertNotEqual(self.regular_movie.price_code, self.new_movie.price_code)
