# Temperature converter
# 1. Asks the user to enter a temperature in Fahrenheit
# 2. Converts it to Celsius using the formula: celsius = (fahrenheit - 32) * 5 / 9
# 3. Prints the result rounded to one decimal place.

fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}\u00B0F is {round(celsius, 1)}\u00B0C")

                                