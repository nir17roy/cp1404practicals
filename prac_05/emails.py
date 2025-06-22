"""
CP1404/CP5632 Practical
Email to name dictionary
"""

def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name_guess = email.split('@')[0].replace('.', ' ').title()
        name = input(f"Name ({name_guess}): ") or name_guess
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


main()
