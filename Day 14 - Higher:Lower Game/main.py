import random
from art import logo,vs
from game_data import data


def random_choose():
    return random.choice(data)

def choosing(person, letter):
    vowel = ['A','E','I','O','U']
    if person["description"][0] in vowel:
        return f"Compare {letter}: {person["name"]}, an {person["description"]}, from {person["country"]}"
    else:
        return f"Compare {letter}: {person["name"]}, a {person["description"]}, from {person["country"]}"

points = 0
continue_game = True
while continue_game:
    account_a = random_choose()
    account_b = random_choose()
    while account_b == account_a:
        account_b = random_choose()

    print(logo)
    print(choosing(account_a, "A"))
    print(vs)
    print(choosing(account_b, "B"))

    answer = input("\nWho has more followers? A or B: ")

    followers_a = account_a["follower_count"]
    followers_b = account_b["follower_count"]

    is_correct = (
        (answer == 'A' and followers_a > followers_b) or
        (answer == 'B' and followers_b > followers_a)
    )

    if is_correct:
        points += 1
        print("\n" * 30)
        print(f"You got it right! You have a score of {points}")
    else:
        print("\n" * 30)
        print(f"Sorry, that was incorrect. You ended with a score of {points}")
        continue_game = False



