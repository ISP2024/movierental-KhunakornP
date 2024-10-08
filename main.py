# Demonstrate the movie rental code.
# Create a customer with some movies and print a statement.

from movie import Movie
from rental import Rental
from customer import Customer


def make_movies():
    """Some sample movies."""
    movies = [
        Movie("Air", Movie.NEW_RELEASE),
        Movie("Oppenheimer", Movie.REGULAR),
        Movie("Frozen", Movie.CHILDRENS),
        Movie("Bitconned", Movie.NEW_RELEASE),
        Movie("Particle Fever", Movie.REGULAR)
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals
    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days = (days + 2) % 5 + 1
    print(customer.statement())
