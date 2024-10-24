# Simple Calculator with Conditionals
# Write a Python program that takes two numbers and an operation (+, -, *, /) from the user.
# Perform the operation and print the result.

# input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# input for an operation
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation based on the inputs
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero is not allowed."
else:
    result = "Invalid operation."

# Print the result
print(f"The result is: {result}")
