"""
This program gets 3 numbers and prints true/false if one of the given numbers is a sum of the other 2 numbers.
"""

a = int(input("Please select number #1:"))
b = int(input("Please select number #2:"))
c = int(input("Please select number #3:"))

if a + b == c or a + c == b or b + c == a:
    print("true")
else: print("false")
