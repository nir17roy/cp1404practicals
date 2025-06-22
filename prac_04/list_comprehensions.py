"""
CP1404/CP5632 Practical
List comprehensions and basic data operations
"""

def main():
    # Get numbers from user input
    numbers_string = input("Enter numbers separated by space: ")
    numbers = [int(num) for num in numbers_string.split()]

    # Get even numbers
    even_numbers = [num for num in numbers if num % 2 == 0]

    # Get squares of the numbers
    squares = [num ** 2 for num in numbers]

    print("Original numbers:", numbers)
    print("Even numbers:", even_numbers)
    print("Squares:", squares)


main()
