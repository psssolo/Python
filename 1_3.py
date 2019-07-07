"""
This program gets a number and prints a pyramid of stars right aligned, with size provided.
"""

x = int(input("Please select a number:"))

for i in range(1, x + 1):
  print("*" * i)
