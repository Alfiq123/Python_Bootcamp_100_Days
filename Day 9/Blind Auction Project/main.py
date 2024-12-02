from art import logo
print(logo)

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

# 💡 User Inputs.
bid_name = str(input("Enter your name: "))
bid_price = int(input("Enter your bid: $"))

# 💡 Store the bidders.
bid_dict = {
    bid_name: bid_price
}

# 💡 Comparing Using max() Function.
# compare = max(zip(bid_dict.values(), bid_dict.keys()))[1]
# print(f"winner is {max(bid_dict, key=bid_dict.get)} with a bid of ${max(bid_dict.values())}")

# 💡 Comparing Using For Loop.
def highest_value(bidding):
    winner = ""
    highest_bid = 0
    for bidder in bidding:
        bid_amount = bidding[bidder]

        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The Winner is {winner} with a bid of ${highest_bid}")

# 💡 Repeat the process.
start_again = True
while start_again:
    decision = str(input("Are there any other bidders?: ")).lower()

    if decision == "yes":
        print("\n" * 100)
        bid_name = str(input("Enter your name: "))
        bid_price = int(input("Enter your bid: $"))
        bid_dict[bid_name] = bid_price

    else:
        start_again = False
        highest_value(bid_dict)
