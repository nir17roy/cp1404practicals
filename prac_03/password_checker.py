"""
CP1404 - Practical
Complete password checker following the instructions.
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIALS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Get a password from user and check if it's valid."""
    show_requirements()
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")

def show_requirements():
    """Display password rules using constants."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIALS_REQUIRED:
        print(f"\tand 1 or more special characters:  {SPECIAL_CHARACTERS}")

def is_valid_password(password):
    """Return True if password meets criteria; otherwise False."""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIALS_REQUIRED and count_special == 0:
        return False

    return True

main()
