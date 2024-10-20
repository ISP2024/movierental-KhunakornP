from pricing import NewRelease, RegularPrice, ChildrenPrice
from typing import Collection
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """
    A movie available for rent.
    """
    
    title = str
    year = int
    genre = Collection[str]

    def is_genre(self, genre: str):
        return genre.lower() in [x.lower() for x in self.genre]

    def get_title(self):
        return self.title
    
    def __str__(self):
        return f"{self.title} ({self.year})"
