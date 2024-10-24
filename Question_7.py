# Triangle Type Checker
# Write a Python program that takes the lengths of three sides of a triangle as input and determines if the triangle is:
# ● Equilateral (all sides are equal),
# ● Isosceles (two sides are equal), or
# ● Scalene (all sides are different).

# inputs for the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Check the type of triangle
if side1 == side2 == side3:
    triangle_type = "Equilateral"
elif side1 == side2 or side2 == side3 or side1 == side3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

# Print the type of triangle
print(f"The triangle is {triangle_type}.")
