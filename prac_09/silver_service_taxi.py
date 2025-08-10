"""
CP1404/CP5632 Practical
SilverServiceTaxi class
"""

from taxi import Taxi

FLAGFALL = 4.50


class SilverServiceTaxi(Taxi):
    """Specialised Taxi with a fanciness level and flagfall."""

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the fare including flagfall."""
        return super().get_fare() + FLAGFALL

    def __str__(self):
        """Return a string representation of the taxi, with fanciness."""
        return f"{super().__str__()} plus flagfall of ${FLAGFALL:.2f}"
