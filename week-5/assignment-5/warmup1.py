"""
Use a for loop with range() to calculate the sum of all integers from 1 to 100. Print the result.
Example output — your message wording might differ:

The sum of 1 to 100 is 5050.
"""
number_sum = 0;
for number in range(1,101):
    number_sum = number_sum + number

print (f"The sum of 1 to 100 is {number_sum}")