# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")
#
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

greet_with("Mustafa", "Chantilly") #positional
greet_with(name = "Mustafa", location = "Chantilly") #keyword


def calculate_love_score(name1, name2):
    name = name1 + name2
    lower_names = name.lower

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    score = first_digit + second_digit
    print(score)


calculate_love_score("mustafa", "badshaha")