"""
Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
Print each key-value pair using .items() in a for loop
Add a new key "graduated" with the value False
Print the updated dictionary
"""

students = {
    "George": {"grade": 6, "subjects": ["reading", "algebra", "art"]},
    "Samantha": {"grade": 1, "subjects": ["reading", "pe", "music"]},
    "Sabrina": {"grade": 12, "subjects": ["literature", "calculus", "physics"]},
}

for name, info in students.items():
    print(f"before update {info}")
    info.update({"graduated": False})
    print(f"after update {info}")

