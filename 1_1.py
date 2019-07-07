"""
This program gets a number from the user and prints out if the number is odd or even.
"""

x = int(input("Please set a number:"))

if x % 2 == 1:
    print(f"{x} is an odd number")
else:
    print(f"{x} is an even number")
