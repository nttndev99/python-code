# Todo-1: Ask the user for input
# Todo-2: Save data into dictionary {name: price}
# Todo-3: Whether if new bids need to be added
# Todo-4: Compare bids in dictionary

from art import logo
print(logo)

def find_highest_bidden(bidding_dctionary):
    winner = ""
    highest_bid = 0

    max(bidding_dctionary)

    for bidder in bidding_dctionary:
        bid_mount = bidding_dctionary[bidder]
        if bid_mount > highest_bid:
            highest_bid = bid_mount
            winner =bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
  
        
bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == "no":
        continue_bidding = False
        find_highest_bidden(bids)
    elif should_continue == "yes":
        print("\n" * 20)