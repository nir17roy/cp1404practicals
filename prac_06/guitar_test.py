"""CP1404/CP5632 Practical - Guitar class test program."""

from guitar import Guitar


def main():
    """Test the Guitar class with some sample data."""
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Fender Stratocaster", 1954, 765.40)

    print(guitar1)
    print(guitar2)


main()
