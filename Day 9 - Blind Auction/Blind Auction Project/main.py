# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)
print("Welcome to the silent auction")

# def max_bid(dictionary):
#     winner = ""
#     highest = 0
#     for bidder in dictionary:
#         bid_amount = bidding_dictionary[bidder]
#         if bid_amount > highest:
#             highest = bid_amount
#             winner = bidder
#
# print(f"The winning bidder is {winner}.")

bidding_dictionary = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("how much would you like to bid?: $"))

    bidding_dictionary[name] = bid

    repeat = input("Are there any other bidders? 'Yes' or 'No: ").lower()

    if repeat == 'no':
        continue_bidding = False
        winner = max(bidding_dictionary, key=bidding_dictionary.get)
        print("\n"*2)
        print(f"The winning bidder is {winner} with a bid of ${bidding_dictionary[winner]}.")
        #max_bid(bidding dictionary)
    else:
        print("\n" * 30)





