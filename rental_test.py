import unittest
from datetime import date
from rental import Rental
from movie import Movie


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two", date.today().year, ["Action"])
		self.regular_movie = Movie("Air", 2022, ["Refreshing"])
		self.childrens_movie = Movie("Frozen", 2022, ["Boring", "Children"])

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air", 2022, ["Refreshing"])
		self.assertEqual("Air", m.get_title())

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
		newer_movie = Movie("The minecraft movie", date.today().year, ["Comedy"])
		rental1 = Rental(newer_movie, 3)
		rental2 = Rental(self.new_movie, 4)
		rental3 = Rental(self.childrens_movie, 5)
		self.assertNotEqual(newer_movie, self.new_movie)
		self.assertEqual(rental1.price_code, rental2.price_code)
		self.assertNotEqual(rental1.price_code, rental3)
