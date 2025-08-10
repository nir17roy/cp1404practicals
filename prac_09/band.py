"""
CP1404/CP5632 Practical
Band class
"""

class Band:
    """Band class represents a band with a name and musicians."""

    def __init__(self, name):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a string showing the band name and its musicians."""
        return f"{self.name} ({', '.join(musician.name for musician in self.musicians)})"

    def play(self):
        """Return a string with all musicians playing their instruments."""
        return "\n".join(musician.play() for musician in self.musicians)
