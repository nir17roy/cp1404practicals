"""
CP1404/CP5632 Practical
UnreliableCar class
"""

import random
from car import Car


class UnreliableCar(Car):
    """A Car that might not drive based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
