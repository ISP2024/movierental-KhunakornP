from pricing import NewRelease, RegularPrice, ChildrenPrice


class Movie:
    """
    A movie available for rent.
    """
    # The types of movies (price_code). 
    NEW_RELEASE = NewRelease()
    REGULAR = RegularPrice()
    CHILDRENS = ChildrenPrice()
    
    def __init__(self, title, price_code):
        # Initialize a new movie. 
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        # get the price code
        return self.price_code

    def get_price(self, days: int) -> float:
        """Delegate to strategy and return the price of the rental"""
        return self.price_code.get_price(days)

    def get_rental_points(self, days: int) -> int:
        """Delegate to strategy and return the points gained"""
        return self.price_code.get_price(days)
    
    def get_title(self):
        return self.title
    
    def __str__(self):
        return self.title
