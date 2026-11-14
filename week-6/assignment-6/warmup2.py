"""
Write two functions:

celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
Call each with a few test values and print the results. Use f-strings and round to one decimal place.

Example output — your test values and wording might differ:

0°C = 32.0°F
100°C = 212.0°F
72°F = 22.2°C
"""

def celsius_to_fahrenheit(c):
    return ((c * 9/5) + 32)

def fahrenheit_to_celsius(f):
    return((f - 32) * 5/9)

def print_temp(temp, temp_unit, result_temp, result_unit):
   print(f" {temp}°{temp_unit} = {round(result_temp, 1)}°{result_unit}")

if __name__ == "__main__":
    print_temp(0,"C",celsius_to_fahrenheit(0),"F")
    print_temp(100, "C", celsius_to_fahrenheit(100), "F")
    print_temp(55, "C", celsius_to_fahrenheit(55), "F")
    print_temp(32, "F", fahrenheit_to_celsius(32), "C")
    print_temp(0, "F", fahrenheit_to_celsius(0), "C")
    print_temp(100, "F", fahrenheit_to_celsius(100), "C")