import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def choosing_cards(hands, deck):
    for i in range(2): #makes sure it does it twice
        hands.append(random.choice(deck)) #randomly choosing cards from deck which is the cards and hands which are the empty lists

def calculate_score(hand):
    check = sum(hand)
    if check == 21 and len(hand) == 2:
        return 0
    while check > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        check = sum(hand)
    return check

replay = input("Do you want to play Blackjack? 'y' or 'n': ").lower()
while replay == 'y':
    print("\n" * 50)
    print(art.logo)
    comp_cards = [] #empty list for computer's hand
    user_cards = [] #empty list for player's hand
    choosing_cards(comp_cards, cards) #perfroming the function ↓
    choosing_cards(user_cards, cards)

    Game = True

    while Game:
        comp_score = calculate_score(comp_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards are {user_cards}")
        print(f"The computer's first card is [{comp_cards[0]},_]")

        if comp_score == 0 or user_score == 0 or user_score > 21:
            Game = False
        else:
            hit = input("\nDo you want to hit or stand? (h)it or (s)tand: ").lower()
            if hit == 'h':
                user_cards.append(random.choice(cards))
            else:
                Game = False


    comp_score = calculate_score(comp_cards)
    user_score = calculate_score(user_cards)

    while comp_score < 17:
        comp_cards.append(random.choice(cards))

        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)
    print(f"\nYour final cards are {user_cards}")
    print(f"The computer's final cards are {comp_cards}")

    def compare(user, comp):
        if user == comp:
             return "\nIt's a Draw"
        if comp == 0:
             return "\nComputer's Blackjack, you lose"
        if user == 0:
            return "\nBlackjack!, You win"
        if user > 21:
            return "\nYou busted"
        if comp > 21:
            return "\nThe computer busted, you win!"
        if comp > user:
            return "\nYou Lose"
        else:
            return "\nYou Win"

    print(compare(user_score, comp_score))

    replay = input("\nDo you want to play again? 'y' or 'n': ")
