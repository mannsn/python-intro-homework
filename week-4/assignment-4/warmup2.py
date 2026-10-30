"""
Create a hardcoded dictionary representing a student with these keys: name, grade, and subjects (a list of subject strings). Then:
Print each key-value pair using .items() in a for loop
Add a new key "graduated" with the value False
Print the updated dictionary
"""

student1 = {"name": "George","grade": 6, "subjects": ["reading", "algebra", "art"]}
print (student1)
  

for name, info in student1.items():
    print(f"key: {name} value: {info}")

student1.update({"graduated": False})

print(f"after update {student1}")


