"""
Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:

The union (all languages from both lists, no duplicates)
The intersection (languages in both lists)
The difference (languages only in the first list)
"""

program_list1 = {"pascal", "c", "java", "c++"}
program_list2 = {"html", "python", "java", "c++", "kotln"}

all_languages = program_list1.union(program_list2)
print(f"all languages = {all_languages}")

common_languages = program_list1.intersection(program_list2)
print(f"intersection languages = {common_languages}")