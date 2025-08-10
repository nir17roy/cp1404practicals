"""
CP1404/CP5632 Practical
Test SilverServiceTaxi
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print(f"Fare: ${fancy_taxi.get_fare():.2f}")

main()
