while True:
    age = int(input("Enter your age? "))
    if age >= 0:
        break
    print("Please enter an age that is zero or positive.")

print("You entered:", age)


if age >= 0 and age <= 12:
	category ="Child"
elif age >= 13 and age <= 17:
	category = "Teen"
elif age >= 18 and age <= 64:
	category = "Adult"
elif age >= 65:
	category = "Senior"
else:
	category = f"No Category found for age {age}, age must be between 0 or greater - error"

print(f"You are a {category}. ")
	