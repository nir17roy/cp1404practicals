"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - When the input can't be turned into an integer (like letters or symbols).

2. When will a ZeroDivisionError occur?
    - If the denominator is 0 when trying to divide.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, by using a loop to keep asking until the user enters a non-zero denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ValueError:
    print("Numerator and denominator must be valid integers!")
print("Finished.")
