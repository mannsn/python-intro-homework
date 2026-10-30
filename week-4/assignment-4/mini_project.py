"""
A data file is provided in week-4/data/roster.py. Copy the students list from that file into your script — it contains dictionaries with name, score, and subject fields.
Using loops and data structure operations, your script must:

Find the top scorer — loop through the list and track the highest score and the name that goes with it. Do not use Python's built-in max() on the list directly.
Calculate the class average — accumulate the total score in a loop, then divide.
List all unique subjects — use a set to collect subjects as you loop, then print them.
List high scorers — use a loop and .append() to get the names of all students who scored above 75.
"""

students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

highest_score = 0;
class_score = 0;
num_class = 0;
class_subjects = set()
high_scorers = []

for student in students:

    #highest score
    if student["score"] > highest_score:
        highest_score = student["score"]
        highest_score_name = student["name"]

    #class average
    class_score = class_score + student["score"]
    num_class = num_class +1

    #unique subjects
    class_subjects.add(student["subject"])


    #high scorers
    if student["score"] > 75:
        high_scorers.append(student["name"])


print(f"The highest score student is {highest_score_name} score: {highest_score}")
print (f"The class average is: {class_score/num_class}")
print (f"The list of unique class subjects is: {class_subjects}")
print (f"The high scoring students with grades above 75 are: {high_scorers}")