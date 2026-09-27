import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
deals = True
agreement = input("Do you want to pay Black Jacket? if yes type 'y' or 'n'\n")

if agreement == 'y':
    user.extend(random.sample(cards, 2))
    computer.extend(random.sample(cards, 2))
    print(f"Your cards: {user}, current score: {sum(user)}")
    print(f" Computer first card is :{computer[0]}")
    if sum(user) == 21 and sum(computer) == 21:
        print("You got Back-Jack first.You won the game")
    elif sum(user) == 21:
        print("You got Back-Jack.You won the game")
    elif sum(computer) == 21:
        print("Computer got Back-Jack.Computer won the game")
    else:
        while agreement == 'y':
            agreement = input("Type 'y' to get another card, type 'n' to pass:")
            if agreement == 'y':
                user.extend(random.sample(cards, 1))
                print(f"Your cards: {user}, current score: {sum(user)}")
                if sum(user) > 21:
                    agreement = 'n'
                    print("You have lost the game")
            else:
                agreement = 'n'
                while sum(computer) < 16:
                    computer.extend(random.sample(cards, 1))
                if sum(computer) > 21:
                    print(f"Your cards: {user}, current score: {sum(user)}")
                    print(f"Computer cards: {computer}, current score: {sum(computer)}")
                    print("You won the game")
                elif sum(user) > sum(computer):
                    print(f"Your cards: {user}, current score: {sum(user)}")
                    print(f"Computer cards: {computer}, current score: {sum(computer)}")
                    print("You won the game")
                else:
                    print(f"Your cards: {user}, current score: {sum(user)}")
                    print(f"Computer cards: {computer}, current score: {sum(computer)}")
                    print("Computer won the game")