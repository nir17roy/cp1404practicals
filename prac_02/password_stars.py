def get_password():
    password = input("Enter the password: ")
    while len(password) < 10:
        print("Password must have at least 10 characters.")
        password = input("Enter the password: ")
    return password


def print_asterisks(password):
    print("*" * len(password))


def main():
    password = get_password()
    print_asterisks(password)


main()
