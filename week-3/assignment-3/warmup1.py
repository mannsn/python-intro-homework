#Letter Grades: Start with a hardcoded score variable (pick any number 0-100). Use if/elif/else to print the corresponding letter grade.
score = 84
if score >= 90 and score <= 100:
    grade = "A"
elif score >= 80 and score <= 89:
    grade = "B"
elif score >= 70 and score <= 79:
    grade = "C"
elif score >= 60 and score <= 69:
    grade = "D"
elif score < 60:
    grade = "F"
else:
    grade = "Error, not in range 0-100"

print (f"Score: {score}, Grade: {grade}")
