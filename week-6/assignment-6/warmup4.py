"""
Write a function is_valid_score(score) that returns True if score is an integer between 0 and 100 (inclusive), and False otherwise. Then use input() to ask the user for a score and convert it to an integer with int() before you check it. Call your function inside an if statement and print either "Valid score." or "Invalid score — must be between 0 and 100.".
"""

def is_valid_score(score):
    result = False
    if (score >= 0 and score <=100):
        result = True
    return (result)


if __name__ == "__main__":
   input_score = int(input("Enter a numeric score: "))
   if is_valid_score(input_score):
       print (f"{input_score}: Valid score")
   else:
      print (f"{input_score}: Invalid score — must be between 0 and 100.")