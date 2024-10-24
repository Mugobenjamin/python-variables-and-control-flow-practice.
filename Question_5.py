# Simple Age Checker
# Write a Python program that asks the user for their age and tells them whether they are a minor (under 18),
# an adult (18-65), or a senior (over 65).

# input your for age
age = int(input("Enter your age: "))

# Check the age category
if age < 18:
    category = "Minor"
elif 18 <= age <= 65:
    category = "Adult"
else:
    category = "Senior"

# Print the age category
print(f"You are a {category}.")
