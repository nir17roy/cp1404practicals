"""
CP1404 - Practical
Temperature Conversion Program
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Main program loop for handling user input and temperature conversion"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = c_to_f(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = f_to_c(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid choice. Please select C, F or Q.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thanks for using the converter!")

def c_to_f(celsius):
    """Takes temperature in Celsius and returns Fahrenheit equivalent"""
    return celsius * 9.0 / 5 + 32

def f_to_c(fahrenheit):
    """Takes Fahrenheit and returns temperature in Celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()
