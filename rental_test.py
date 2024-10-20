import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class RentalTest(unittest.TestCase):

	def setUp(self):
		self.new_movie = Movie("Dune: Part Two")
		self.regular_movie = Movie("Air")
		self.childrens_movie = Movie("Frozen")

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("Air")
		self.assertEqual("Air", m.get_title())

	def test_rental_price(self):
		"""Test the price for different kinds of movies"""
		# test new movies
		rental = Rental(self.new_movie, 1, NewRelease())
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5, NewRelease())
		self.assertEqual(rental.get_price(), 15.0)
		# test regular movies
		rental = Rental(self.regular_movie, 2, RegularPrice())
		self.assertEqual(rental.get_price(), 2.0)
		rental = Rental(self.regular_movie, 5, RegularPrice())
		self.assertEqual(rental.get_price(), 6.5)
		# test children movies
		rental = Rental(self.childrens_movie, 2, ChildrenPrice())
		self.assertEqual(rental.get_price(), 1.5)
		rental = Rental(self.childrens_movie, 5, ChildrenPrice())
		self.assertEqual(rental.get_price(), 4.5)

	def test_rental_points(self):
		"""Test the rental point gain for different movie types"""
		# test children movies
		rental = Rental(self.childrens_movie, 1, ChildrenPrice())
		self.assertEqual(rental.rental_points(), 1)
		# die hard frozen fans still only get 1 point per rental
		rental = Rental(self.childrens_movie, 99, ChildrenPrice())
		self.assertEqual(rental.rental_points(), 1)
		# test regular movies
		rental = Rental(self.regular_movie, 1, RegularPrice())
		self.assertEqual(rental.rental_points(), 1)
		# still only 1 point per rental
		rental = Rental(self.regular_movie, 420, RegularPrice())
		self.assertEqual(rental.rental_points(), 1)
		# test new movies
		rental = Rental(self.new_movie, 1, NewRelease())
		self.assertEqual(rental.rental_points(), 1)
		# new movies get more points per day rented
		rental = Rental(self.new_movie, 50, NewRelease())
		self.assertEqual(rental.rental_points(), 50)

	def test_movies(self):
		"""
		Movies should be different objects but have the same PriceStrategy
		if their types are the same.
		"""
		newer_movie = Movie("The minecraft movie")
		self.assertNotEqual(newer_movie, self.new_movie)
