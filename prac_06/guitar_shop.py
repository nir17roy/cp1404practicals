"""CP1404/CP5632 Practical - Guitar shop program."""

from guitar import Guitar


def main():
    """Get details of guitars from user, store and display them."""
    guitars = []

    print("My guitars!")
    name = input("Name: ")

    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.\n")
        name = input("Name: ")

    # Display all guitars
    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            print(f"Guitar {i}: {guitar}")
    else:
        print("No guitars added.")


main()
