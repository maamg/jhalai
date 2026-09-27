# import random
#
# user_card = []
# computer_card = []
# is_game_over = False
#
#
# def deal_card(user):
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     user.extend(random.sample(cards, 1))
#
#
# def calculate_score(cardList):
#     if len(cardList) == 2 and sum(cardList) == 21:
#         return 0
#     else:
#         return sum(cardList)
#
#
# def compare(user, computer):
#     if calculate_score(user) > calculate_score(computer):
#         print(f" Your card: [{user} and your score: {sum(user)} ")
#         print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
#         print("You won the game")
#     elif calculate_score(user) < calculate_score(computer):
#         print(f" Your card: [{user} and your score: {sum(user)} ")
#         print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
#         print("You lost the game")
#     else:
#         print(f" Your card: [{user} and your score: {sum(user)} ")
#         print(f" Computer's card: [{computer}] and computer's score:{sum(computer)}")
#         print("It's Tie")

is_game_over = False


def play_game():
    global is_game_over
    if not is_game_over:
        first_agreement = input("If 'y' is given, next code will be executed\n")
        while first_agreement == 'y':
            second_agreement = input("If 'n' is given else block will be executed\n")
            if second_agreement == 'n':
                first_agreement = 'n'
        else:
            print("Else Block is executed")
            is_game_over = True


play_game()





