# Python Calculator
"""
operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1/num2
    print(round(result, 2))
else:
    print(f"{operator} is not a valid operator")
"""

weight = float(input("enter your weight "))
unit = input("kilograms or pounds? (K or L): ")


if unit == "K":
    weight *= 2.205
    unit = "Lbs."
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
else:
    print(f"{unit} was not valid")

print (f"Your weight is: {round(weight, 1)} {unit}")

