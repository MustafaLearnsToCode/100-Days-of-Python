letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random
def terminate():
    if nr_symbols + nr_letters > nr_letters:
        print("Error too many characters")
        return
    elif nr_numbers + nr_letters > nr_letters:
        print("Error too many characters")


print("Welcome to the PyPassword Generator!")
total = input("How many characters would you like in your password?\n")
nr_letters = int(input("How many letters would you like?\n"))
terminate()
nr_symbols = int(input(f"How many symbols would you like?\n"))
terminate()
nr_numbers = int(input(f"How many numbers would you like?\n"))
terminate()

# for i in range(nr_letters):
#     (random.shuffle(letters))
#     print(letters[0], end="")
#
# for i in range(nr_symbols):
#     (random.shuffle(symbols))
#     print(symbols[0], end="")
#
# for i in range(nr_numbers):
#     (random.shuffle(numbers))
#     print(numbers[0], end="")

password = []

for i in range(nr_letters):
    password.append(random.choice(letters))

for i in range(nr_symbols):
    password.append(random.choice(symbols))

for i in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
print(f"Your password is:{''.join(password)}")





