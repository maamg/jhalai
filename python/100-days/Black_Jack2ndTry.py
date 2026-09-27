import random
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
dealer = []
deals = True

while deals:
    agreement = input("Do you want to play BlackJack? Type 'y' or 'n'\n")
    if agreement == 'y':
        user.extend(random.sample(card, 2))
        print(f"Your cards: {user}, current score: {sum(user)}")

        dealer.extend(random.sample(card, 1))
        print(f"Computer's first card is {dealer[0]}")
        if sum(user) > 21:
            deals = False
    else:
        deals = False

while sum(dealer) <= 16:
    dealer.extend(random.sample(card, 1))

print(dealer)