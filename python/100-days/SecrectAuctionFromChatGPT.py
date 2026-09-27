bids = {}
highest_bid = 0
highest_bidder = ""
bid_limit = 1000

def register_bidder(name, bid):
    global highest_bid, highest_bidder
    if bid > bid_limit:
        print(f"Bid amount exceeded the limit of ${bid_limit}.")
        return
    if bid <= 0:
        print("Bid amount should be greater than zero.")
        return
    if name in bids:
        print("You have already placed a bid.")
        return
    bids[name] = bid
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name
    print(f"Bid placed successfully! {name} bid ${bid}.")

def check_bids():
    if not bids:
        print("No bids placed yet.")
        return
    print("Current bids:")
    for name, bid in bids.items():
        print(f"{name} - ${bid}")

def end_auction():
    global highest_bid, highest_bidder
    if not bids:
        print("No bids placed. Ending auction.")
        return
    print(f"Auction ended. The winner is {highest_bidder} with a bid of ${highest_bid}.")

if __name__ == "__main__":
    print("Welcome to the secret auction program.")
    while True:
        name = input("What is your name?: ")
        bid = int(input("What is your bid?: $"))
        register_bidder(name, bid)
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            end_auction()
            break
        elif should_continue == "yes":
            check_bids()
