# a. Print odd numbers from 1 to 20
print("a. Odd numbers from 1 to 20:")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# b. Count in 10s from 0 to 100
print("b. Counting in 10s from 0 to 100:")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# c. Count down from 20 to 1
print("c. Counting down from 20 to 1:")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# d. Print n stars on one line
n = int(input("Number of stars: "))
print("d. Stars on one line:")
for i in range(n):
    print("*", end='')
print()

# e. Print lines of increasing stars using nested loop
print("e. Increasing stars pattern (nested loop):")
for i in range(n + 1):
    for j in range(i):
        print("*", end='')
    print()
