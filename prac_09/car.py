"""
CP1404/CP5632 Practical
Car class
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if it has enough fuel.

        Drive given distance or drive until fuel runs out.
        Return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
        self.fuel -= distance
        self.odometer += distance
        return distance
