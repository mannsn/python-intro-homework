"""
A data file is provided in week-5/data/numbers.py. Copy the numbers list from that file into your script.
Build a menu-driven program using a while loop. Each time the menu displays, the user picks an option. The menu below shows the format — your wording and layout might differ, but all five options must be present:
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5):
Requirements for each option:
Find minimum — loop through the list and track the smallest value. Do not use Python's built-in min().
Find maximum — same approach, tracking the largest value. Do not use max().
Search — ask the user for a number, then implement a linear search loop. Print the index if found, or a "not found" message.
Sort — implement bubble sort: repeatedly loop through adjacent pairs, swap if out of order, and repeat until no swaps occur. Print the sorted list. Do not use sorted() or .sort().
Quit — print a goodbye message and exit the loop.
The menu should redisplay after each operation until the user chooses Quit.

Bubble sort hint: One pass through the list looks at pairs — numbers[i] and numbers[i+1] — and swaps them if the first is larger. You need to repeat this process until a full pass produces zero swaps.
Pseudocode:

repeat:
    swapped = False
    for each adjacent pair:
        if left > right:
            swap them
            swapped = True
until swapped is False
"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# Get menu option

while True:
    # Create menu
    print(f"\n=== Number Cruncher ===")
    print(f"1. Find minimum")
    print(f"2. Find maximum")
    print(f"3. Search for a number")
    print(f"4. Sort the list")
    print(f"5. Quit")
    menu_number = input("Choose an option (1-5): ")

    if menu_number.isdigit():
        menu_number = int(menu_number)

        if (menu_number > 0 and menu_number) < 6:

            # Find minimum
            if menu_number == 1:
                print(f"\nList of numbers = {numbers}")
                min_number = 100
                for number in numbers:
                    if number < min_number:
                        min_number = number
                print(f"Minimum number = {min_number}")

            # Find maximum
            elif menu_number == 2:
                print(f"\nList of numbers = {numbers}")
                max_number = 0
                for number in numbers:
                    if number > max_number:
                        max_number = number
                print(f"Maximum number = {max_number}")

            # Search for a number
            elif menu_number == 3:
                print(f"\nList of numbers = {numbers}")
                search_number = input("Enter a number to search: ")

                if search_number.isdigit():
                    search_number = int(search_number)
                    index = 0
                    found = False
                    for number in numbers:
                        index += 1
                        if number == search_number:
                            print(f"Index of search number {search_number} = {index}")
                            found = True
                            break
                    if not found:
                        print(f"Search number {search_number} not found")
                else:
                    print(f"Search number must be a digit, try again.")

            elif menu_number == 5:
                print("Good bye - you selected quit")
                break

        else:
            print("Menu option not in range 1-5, Try again")

    else:
        print("Menu option not in range 1-5, Try again")
