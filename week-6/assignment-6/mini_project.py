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


Open your mini_project.py from Assignment 5. You're going to refactor it so that each operation lives in its own function.
Create a new file (don't modify your Week 5 submission). Pull a copy of the numbers list from week-5/data/numbers.py into your new script.
Define the following functions, each taking numbers (a list) as a parameter:
find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
search(numbers, target) — returns the index of target, or -1 if not found
bubble_sort(numbers) — returns a new sorted list (do not modify the original)
show_menu() — prints the menu options and returns the user's choice as a string
main() — the while loop that calls show_menu() and dispatches to the right function
Call main() at the bottom of the file.
Requirements:
No logic should live outside of a function (except the numbers list definition and the main() call)
bubble_sort should return a new list, not sort in place
Your search function should print "Found at index X" or "Not found" from inside main(), not inside search() itself — search just returns the index
Save as: mini_project.py
"""

numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


def find_min(numbers):
    """
    find_min(numbers) — returns the minimum value (your loop-based implementation, no min())
    """
    min_number = numbers[0]
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number


def find_max(numbers):
    """
    find_max(numbers) — returns the maximum value (your loop-based implementation, no max())
    """
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


def search(numbers, target):
    """
    search(numbers, target) — returns the index of target, or -1 if not found
    """
    index = 0
    found = False
    for number in numbers:

        if number == target:
            found = True
            break
        index = index + 1
    if not found:
        index = -1
    return index


def bubble_sort(numbers):
    """
    bubble_sort(numbers) — returns a new sorted list (do not modify the original)
    """
    swapped = True
    sorted_list = numbers.copy()

    while swapped:

        swapped = False

        for index in range(len(sorted_list) - 1):

            firstNum = sorted_list[index]
            secondNum = sorted_list[index + 1]

            if firstNum > secondNum:
                sorted_list[index], sorted_list[index + 1] = (
                    sorted_list[index + 1],
                    sorted_list[index],
                )
                swapped = True
    return sorted_list


def show_menu():
    """
    show_menu() — prints the menu options and returns the user's choice as a string
    """
    # Create menu
    print(f"\n=== Number Cruncher ===")
    print(f"1. Find minimum")
    print(f"2. Find maximum")
    print(f"3. Search for a number")
    print(f"4. Sort the list")
    print(f"5. Quit")
    menu_number = input("Choose an option (1-5): ")
    return menu_number


def main():
    """
    main() — the while loop that calls show_menu() and dispatches to the right function
    """
    while True:
        # Create menu
        menu_number = show_menu()

        if menu_number.isdigit():
            menu_number = int(menu_number)

            if menu_number > 0 and menu_number <= 5:

                # Find minimum
                if menu_number == 1:
                    print(f"\nList of numbers = {numbers}")
                    print(f"Minimum number = {find_min(numbers)}")

                # Find maximum
                elif menu_number == 2:
                    print(f"\nList of numbers = {numbers}")
                    print(f"Maximum number = {find_max(numbers)}")

                # Search for a number
                elif menu_number == 3:
                    print(f"\nList of numbers = {numbers}")
                    search_number = input("Enter a number to search: ")

                    if search_number.isdigit():

                        target = int(search_number)
                        index = search(numbers, target)
                        if index != -1:
                            print(f"Index of search number {target} = {index}")
                        else:
                            print(f"Search number {target} not found")
                    else:
                        print(f"Search number must be a digit, try again.")

                # Sort
                elif menu_number == 4:
                    print(f"\nList of numbers = {numbers}")
                    new_list = bubble_sort(numbers)

                    print(f"\nSorted list of numbers = {new_list}")

                elif menu_number == 5:
                    print("Good bye - you selected quit")
                    break

            else:
                print("Menu option not in range 1-5, Try again")

        else:
            print("Entered non digit. Menu option not in range 1-5, Try again")


if __name__ == "__main__":
    # Get menu option

    main()
