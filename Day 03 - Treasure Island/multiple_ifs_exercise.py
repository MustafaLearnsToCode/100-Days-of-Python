print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Child tickets are $5.")
        bill = 5
    elif age <= 18:
        print("Youth tickets are $7.")
        bill = 7
    else:
        print("Adult tickets are $12.")
        bill = 12

    photo = input("Do you want a photo taken? Type Y for yes and N for no: ")
    if photo == "Y":
        bill += 3
    print(f"Your final bill is {bill} dollars")
else:
    print("Sorry you have to grow taller before you can ride.")
