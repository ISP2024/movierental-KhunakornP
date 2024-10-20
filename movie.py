from typing import Collection
from dataclasses import dataclass
import csv
import logging


movie_logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    
    title: str
    year: int
    genre: Collection[str]

    def is_genre(self, genre: str):
        return genre.lower() in [x.lower() for x in self.genre]

    def get_title(self):
        return self.title
    
    def __str__(self):
        return f"{self.title} ({self.year})"


class MovieCatalog:
    """A factory for creating movies."""
    _instance = None
    _movies = []
    _movie_data = None
    _movie_generator = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._movie_data = csv.reader(open("movies.csv"))
            cls._movie_generator = cls.movie_generator()
        return cls._instance

    def get_movie(self, title: str, year: int = None):
        """Get the first matching movie from the catalogue."""
        # try to find the movies in catalog first
        for movie in self._movies:
            if self.search_movie(movie, title, year):
                return movie

        # movie was not found try reading from data file
        for movie in self._movie_generator:
            if self.search_movie(movie, title, year):
                return movie

        # No movie found
        return None

    @staticmethod
    def search_movie(movie: Movie,  title: str, year: int = None) -> bool:
        """Check if the movie has the title and year provided."""
        return (movie.title.lower() == title.lower() and
                (year is None or year == movie.year))

    @classmethod
    def movie_generator(cls):
        """Generator for getting movies"""
        next(cls._movie_data)  # skip the column names
        for row in cls._movie_data:
            if len(row) < 1 or row[0][0] == "#":  # blank row or comment
                continue
            try:
                movie = Movie(row[1],
                              row[2],
                              [x for x in row[3].split("|")])
                cls._movies.append(movie)
                yield movie
            except (IndexError, ValueError, TypeError):
                movie_logger.error(
                    f'Line {cls._movie_data.line_num}: '
                    f'Unrecognized format "{", ".join(row)}"')
