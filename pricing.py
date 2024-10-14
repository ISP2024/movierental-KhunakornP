from abc import ABC, abstractmethod


class PriceStrategy(ABC):
    """Abstract base class for rental pricing."""
    _instance = None

    @abstractmethod
    def get_price(self, days: int) -> float:
        """Get the price of this movie rental."""
        raise NotImplementedError

    @abstractmethod
    def get_rental_points(self, days: int) -> int:
        """Get the rental points earned for this rental."""
        raise NotImplementedError

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class NewRelease(PriceStrategy):
    """Pricing and rental point rules for New Release movies."""

    def get_rental_points(self, days: int) -> int:
        """New release rentals earn 1 point for each day rented."""
        return days

    def get_price(self, days: int) -> float:
        """Straight $3 per day charge"""
        return 3.0 * days


class RegularPrice(PriceStrategy):
    """Pricing and rental point rules for Regular movies."""

    def get_rental_points(self, days: int) -> int:
        """Regular movies get 1 point per rental"""
        return 1

    def get_price(self, days: int) -> float:
        """Two days for $2, additional days 1.50 per day."""
        if days > 2:
            return 2.0 + ((days - 2) * 1.5)
        return 2.0


class ChildrenPrice(PriceStrategy):
    """Pricing and rental point rules for children movies."""

    def get_rental_points(self, days: int) -> int:
        """Children movies get 1 point per rental"""
        return 1

    def get_price(self, days: int) -> float:
        """Three days for $1.50, additional days 1.50 per day."""
        if days > 3:
            return 1.5 + ((days - 3) * 1.5)
        return 1.5