try:
    age = int(input("How old are you? "))
except ValueError:
    print("Invalid input. Please type in a numerical value like 16")
    age = int(input("How old are you? "))
if age > 18:
    print(f"You can drive at age {age}.")
