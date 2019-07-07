"""
This program gets a number and prints a pyramid of stars center aligned, with size provided.
"""

x = int(input("Please select a number:"))

for i in range(1, x * 2 + 1, 2):
  print(("*" * i).center(x * 2 - 1))
