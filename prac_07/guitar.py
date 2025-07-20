"""CP1404/CP5632 Practical - Guitar class."""


CURRENT_YEAR = 2023


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage (50+ years old)."""
        return self.get_age() >= 50

    def __str__(self):
        """Return string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"
