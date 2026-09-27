bid_dic = {}
bidding_finished = False

while bidding_finished == False:
    print("Welcome to the secret auction program.")
    name = input("What is your name?:")
    bid_amount = int(input("What's your bid?: $"))
    bidder = input("Are there any other bidders? Type 'yes' or 'no'.")

    if bidder == 'no':
        bidding_finished = True
    bid_dic[name] = bid_amount

winner_amount = 0
winner = ''
for person in bid_dic:
    while bid_dic[person] > winner_amount:
        winner_amount = bid_dic[person]
        winner = person
print(f"The winner is {winner} with a bid of ${winner_amount}")