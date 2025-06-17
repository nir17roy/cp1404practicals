"""
CP1404 - Practical
Program that evaluates the quality of a score and handles random scoring
"""

import random

def main():
    """Main routine to take user input and display score evaluation"""
    try:
        score = float(input("Enter score: "))
        result = evaluate_score(score)
        print(result)
        generate_random_score()
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def evaluate_score(score):
    """Returns a performance message based on the score value"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def generate_random_score():
    """Generates a random score and evaluates it using evaluate_score"""
    number = random.randint(0, 100)
    print(number)
    print(evaluate_score(number))

main()
