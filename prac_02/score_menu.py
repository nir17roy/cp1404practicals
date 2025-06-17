import random

MENU = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""

def main():
    """Handles the main menu loop for the program"""
    print(MENU)
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(f"Score: {score}")
        elif choice == "P":
            user_input = float(input("Give score: "))
            print(f"Result: {evaluate_score(user_input)}")
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid selection. Please choose again.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye!")

def evaluate_score(score):
    """Returns a message based on score classification"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def display_stars(score):
    """Prints one asterisk per point of score"""
    print("*" * score)

def get_valid_score():
    """Generates and returns a random score between 0 and 100"""
    return random.randint(0, 100)

main()
