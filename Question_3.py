# Grade Categorizer
#Write a program that takes a score (0-100) as input and categorizes it into one of the following grades:
# ● A (90-100)
# ● B (80-89)
# ● C (70-79)
# ● D (60-69)
# ● F (below 60)

# User inputs a score
score = int(input("Enter the score (0-100): "))

# Arrange the score into a grades
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid score'

# Print the grade
print(f"Your grade is: {grade}")

