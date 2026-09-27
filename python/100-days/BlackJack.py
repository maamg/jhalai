import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
user.extend(random.sample(cards, 2))
computer.extend(random.sample(cards, 2))
chalavilable = True
while chalavilable:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
        print(f"Your card is {user}, current score is {sum(user)}")
        print(f"Computer's first card is: {computer[0]}")
        while sum(computer) < 21 or sum(user) < 21:
            if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
                user.append(random.choice(cards))
                computer.append(random.choice(cards))
                print(f"Your card is {user}, current score is {sum(user)} \n")
                print(f"Computer's first card is: {computer[0]}")

            else:
                chalavilable = False
        if sum(computer) > 21:
            print(f"Computer exceed 21,{computer}")
            print("You won the game")
            chalavilable = False
        elif sum(user) > 21:
            print(f"Your point exceed 21, {user}")
            print(f"Computer won the game")
            chalavilable = False

    else:
        chalavilable = False

if sum(user) > sum(computer):
    print(f"Your point is {sum(user)} and Computer's Point is {sum(computer)}")
    print("You won the game")

elif sum(computer) > sum(user):
    print(f"Your point is {sum(user)} and Computer's Point is {sum(computer)}")
    print("You lose the game")

else:
    print(f"Your total score : {sum(user)} and computer total score: {sum(computer)}")
    print("Push!")