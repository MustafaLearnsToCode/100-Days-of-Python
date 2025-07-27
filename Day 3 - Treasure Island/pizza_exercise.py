print("Welcome to Python Pizza Deliveries!")
bill = 0

size = input("What size pizza do you want? S, M or L: ")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("We don't have that size")

pep = input("Do you want to add pepperoni? Y or N: ")
if pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

cheese = input("Do you want extra cheese? Y or N: ")
if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")