number = int(input("Enter a number? "))

if number == 0:
    print(f"{number} is neither positive or negative")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is positive")

if number % 2 == 0:
    print(f"{number} is even")
else:
    print (f"{number} is odd")
