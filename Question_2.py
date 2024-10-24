# Odd or Even Checker
# Write a Python program that asks the user for a number and then prints whether the number is odd or even.

# Ask the user to input a number
number = int(input("Enter a number: "))

# Check if the number is odd or even using the modulo % sign
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
