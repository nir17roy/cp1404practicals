"""CP1404/CP5632 Practical - Guitar inventory program."""

from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Load guitars, let user add new ones, and save them."""
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded from file:")
    display_guitars(guitars)

    print("\nAdd new guitars:")
    guitars += get_new_guitars()

    print("\nThese are the final guitars:")
    display_guitars(guitars)

    save_guitars(FILENAME, guitars)


def load_guitars(filename):
    """Read guitars from CSV and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        next(in_file)  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars in a formatted table."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")


def get_new_guitars():
    """Prompt user to enter new guitars, return them as a list."""
    new_guitars = []
    name = input("Name: ")
    while name != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitar = Guitar(name, year, cost)
            new_guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input. Please enter numeric values for year and cost.")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Save list of Guitar objects to CSV file."""
    with open(filename, 'w') as out_file:
        out_file.write("Name,Year,Cost\n")
        for guitar in guitars:
            print_line = f"{guitar.name},{guitar.year},{guitar.cost}\n"
            out_file.write(print_line)


if __name__ == "__main__":
    main()
