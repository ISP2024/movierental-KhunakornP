"""Test cases for determining price codes"""
import unittest
from movie import Movie
from rental import Rental
from datetime import date
from pricing import ChildrenPrice, RegularPrice, NewRelease


class PricingTest(unittest.TestCase):
    def test_get_price_for_new_movie(self):
        """Movies created this year should have NewRelease price code."""
        blockbuster1 = Movie("Clinic of horrors",
                             date.today().year,
                             ["Horror", "Action"])
        blockbuster2 = Movie("Don Quixote",
                             date.today().year,
                             ["Comedy", "Action"])
        rental1 = Rental(blockbuster1, 5)
        rental2 = Rental(blockbuster2, 3)
        self.assertEqual(rental1.price_code, NewRelease())
        self.assertEqual(rental2.price_code, NewRelease())
        self.assertEqual(rental1.price_code, rental2.price_code)

    def test_get_price_for_children_movie(self):
        """
        Movies with the 'Children' and 'Childrens' genre are children movies.
        """
        movie1 = Movie("Garfield on ice",
                       2020,
                       ["Comedy", "Action", "Children"])
        movie2 = Movie("The amazing movie of Gumball",
                       2025,
                       ["Childrens", "Comedy", "Thriller"])
        rental1 = Rental(movie1, 5)
        rental2 = Rental(movie2, 3)
        self.assertEqual(rental1.price_code, ChildrenPrice())
        self.assertEqual(rental2.price_code, ChildrenPrice())
        self.assertEqual(rental1.price_code, rental2.price_code)

    def test_get_price_for_regular_movie(self):
        """Other Movies have RegularPrice price code."""
        movie1 = Movie("The stanley parable movie",
                       2020,
                       ["Comedy", "Action", "Psychological horror"])
        movie2 = Movie("The rise of the Yamana clan",
                       2025,
                       ["Action", "Thriller"])
        rental1 = Rental(movie1, 5)
        rental2 = Rental(movie2, 3)
        self.assertEqual(rental1.price_code, RegularPrice())
        self.assertEqual(rental2.price_code, RegularPrice())
        self.assertEqual(rental1.price_code, rental2.price_code)


