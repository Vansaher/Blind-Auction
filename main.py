# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art

print(art.logo)
print("Welcome to the secret auction program.")

bidder_available = True
bids = {}
while bidder_available:
    name = input("What is your name?")
    amount = float(input("What's your bid? $"))

    bids[name] = amount

    moreBidders = input("Are there any other bidders? Type 'Yes' or 'no'. \n")

    if moreBidders.lower() == "yes":
        print("\n" * 20)
    else:
        bidder_available = False

print("\nBidding has ended. Here are the bids:")
for name, amount in bids.items():
    print(f"{name}: ${amount}")

highest_bidder = max(bids, key=bids.get)
highest_amount = bids[highest_bidder]
print(f"No more bids, the winner is {highest_bidder} with a bid of ${highest_amount:.2f}")
