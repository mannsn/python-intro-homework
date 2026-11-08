"""
Use a while loop that repeatedly asks the user to enter a positive integer. If the user enters anything that isn't a positive integer, print a message and ask again. Once valid input is received, print it and stop. The example session below shows the format — your inputs and message wording might differ:
"""



while True:
    number = (input("Enter a positive integer? "))

    if number.isdigit():
      number = int(number)
      if number > 0:
          break
      print("That's not a positive integer. Try again.")
    else:
       print("That's not a positive integer. Try again.")

print(f"Got it: {number} ")