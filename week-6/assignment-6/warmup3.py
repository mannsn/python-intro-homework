"""
Demonstrate variable scope with two short examples in one file:

Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.
Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.
Save as: warmup3.py

"""


def variable_demo():
    inside = 2
    return (inside)


if __name__ == "__main__":
    # NameError: name 'inside' is not defined
    #print (inside)

    print(f"{variable_demo()}")

 