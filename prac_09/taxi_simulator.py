"""
CP1404/CP5632 Practical
Taxi simulator using inheritance
"""

from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi

def main():
    """Run the taxi simulator program."""
    taxis = [
        Taxi("Prius 1", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]

    total_bill = 0
    current_taxi = None

    menu = "q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            print("Taxis available:")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")

        elif choice == "d":
            if current_taxi:
                distance = int(input("Drive how far? "))
                current_taxi.start_fare()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(menu)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()
