import re
import unittest
from customer import Customer
from rental import Rental
from movie import Movie
from pricing import ChildrenPrice, RegularPrice, NewRelease


class CustomerTest(unittest.TestCase):
	""" Tests of the Customer class"""

	def setUp(self):
		"""Test fixture contains:

		c = a customer
		movies = list of some movies
		"""
		self.c = Customer("Movie Mogul")
		self.new_movie = Movie("Mulan")
		self.regular_movie = Movie("CitizenFour")
		self.childrens_movie = Movie("Frozen")

	def test_billing(self):
		"""Test the total charge of customers"""
		customer = Customer("Window wayne")
		# customer has not rented anything yet
		self.assertEqual(customer.get_total_charge(), 0)
		customer.add_rental(Rental(self.new_movie, 4, NewRelease()))
		# new movie costs 3 * 4 = 12$
		self.assertEqual(customer.get_total_charge(), 12)
		customer.add_rental(Rental(self.childrens_movie, 5, ChildrenPrice()))
		# also rent frozen for 5 days
		# total charge = 1.5 + 2*1.5 + 12 = 16.5$
		self.assertEqual(customer.get_total_charge(), 16.5)

	def test_point_gain(self):
		"""Test the total points earned from renting"""
		customer = self.c
		self.assertEqual(customer.get_total_points(), 0)
		customer.add_rental(Rental(self.childrens_movie, 5, ChildrenPrice()))
		# not a new movie only 1 point earned
		self.assertEqual(customer.get_total_points(), 1)
		customer.add_rental(Rental(self.new_movie, 5, NewRelease()))
		# new movie gains 1 point per day rented
		self.assertEqual(customer.get_total_points(), 6)

	def test_statement(self):
		stmt = self.c.statement()
		# get total charges from statement using a regex
		pattern = r".*Total [Cc]harges\s+(\d+\.\d\d).*"
		matches = re.match(pattern, stmt, flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("0.00", matches[1])
		# add a rental
		self.c.add_rental(Rental(self.new_movie, 4, NewRelease())) # days
		stmt = self.c.statement()
		matches = re.match(pattern, stmt.replace('\n',''), flags=re.DOTALL)
		self.assertIsNotNone(matches)
		self.assertEqual("12.00", matches[1])
