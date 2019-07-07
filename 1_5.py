"""
This program reads two numbers and an operator and returns the calculation result.
"""

def get_input_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("wrong number input, try again")


def calc(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return  a / b
    elif operator == "^":
        return a ** b
    else:
        return None


num1 = get_input_number("Please select number #1:")
num2 = get_input_number("Please select number #2:")

while True:
    operator_input = input("Please select operator (+ - * / ^):")
    result = calc(num1, num2, operator_input)
    if result is None:
        print("wrong operator input, try again")
    else:
        print(f"Result: {num1} {operator_input} {num2} = {result}")
        break




