# CP1404 - Practical
# File reading/writing tasks following set instructions.

# 1. Ask for the user's name and save it to 'name.txt'
user_name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(user_name)
file.close()

# 2. Read back the name from 'name.txt' and greet the user
file = open("name.txt", "r")
saved_name = file.read().strip()
file.close()
print(f"Hi {saved_name}!")

# 3. Read the first two numbers from 'numbers.txt', add them, and print the result
with open("numbers.txt", "r") as f:
    lines = f.readlines()
    first_two_total = int(lines[0]) + int(lines[1])
    print(first_two_total)

# 4. Read all numbers from 'numbers.txt', sum them, and print the total (ignore blank lines)
total = 0
with open("numbers.txt", "r") as f:
    for line in f:
        number = line.strip()
        if number:  # only convert if not empty
            total += int(number)
    print(total)
