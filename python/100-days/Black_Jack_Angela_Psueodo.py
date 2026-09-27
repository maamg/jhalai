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
#
#
# def play_game():
#     global is_game_over
#     if not is_game_over:
#         first_agreement = input("Do you want to play Black-Jack.Type 'y' to play and type 'n' to exit\n")
#         while first_agreement == 'y':
#             deal_card(user_card)
#             deal_card(computer_card)
#             deal_card(user_card)
#             deal_card(computer_card)
#             if calculate_score(user_card) == 0 and calculate_score(computer_card) ==0:
#                 print(f"You have the Black-Jack [{user_card}] first! You win")
#             elif calculate_score(user_card) == 0 and calculate_score(computer_card) != 0:
#                 print(f"You have the Black-Jacket{user_card}.Computer win")
#             elif calculate_score(user_card) != 0 and calculate_score(computer_card) == 0:
#                 print(f'Computer has the Black Jacket {computer_card}. Computer won the game')
#             else:
#                 print(f" Your card is {user_card} and computer's first card is [{computer_card[0]}]")
#                 while first_agreement == 'y':
#                     agreement = input("Type 'y' to get another card, type 'n' to pass:\n")
#                     if agreement == "y":
#                         deal_card(user_card)
#                         print(f"Your card is {user_card}, and your score is {calculate_score(user_card)} ")
#                         if calculate_score(user_card) == 21:
#                             print("Yes! You have got the Black-Jack")
#                             is_game_over = True
#                         elif calculate_score(user_card) < 21:
#                             first_agreement = 'y'
#                         else:
#                             print("You have exceed 21!")
#                             is_game_over = True
#                     else:
#                         first_agreement = False
#                         print("agreement = 'n'")
#
#                 while calculate_score(computer_card) < 17:
#                     deal_card(computer_card)
#                     is_game_over = False
#
#                 if calculate_score(computer_card) > 21:
#                     print(f"Computer exceed score 21. Computer's card :{computer_card} and computer score is: [{calculate_score(computer_card)}]")
#                     is_game_over = True
#
#                 else:
#                     if calculate_score(user_card) > calculate_score(computer_card):
#                         print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
#                         print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
#                         print(" You won the game")
#                         is_game_over = True
#
#                     elif calculate_score(user_card) < calculate_score(computer_card):
#                         print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
#                         print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
#                         print(" You lost the game")
#                         is_game_over = True
#
#                     elif calculate_score(user_card) == calculate_score(computer_card):
#                         print(f"Your card is {user_card} and score: [{calculate_score(user_card)}]")
#                         print(f"Computer card is {computer_card} and score: [{calculate_score(computer_card)}]")
#                         print(" It's a draw")
#                         is_game_over = True
#
#
# play_game()
#
#
#
#
#


# import random
#
#
# def deal_card():
#     """Returns a random card from the deck."""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# # Hint 6: Create a function called calculate_score() that takes a List of cards as input
# # and returns the score.
# # Look up the sum() function to help you do this.
# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#
#     # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
#     # instead of the actual score. 0 will represent a blackjack in our game.
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#     # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and
#     # replace it with a 1. You might need to look up append() and remove().
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#     return sum(cards)
#
#
# # Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# # both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# # has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# # is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
# def compare(user_score, computer_score):
#     # Bug fix. If you and the computer are both over, you lose.
#     if user_score > 21 and computer_score > 21:
#         return "You went over. You lose 😤"
#
#     if user_score == computer_score:
#         return "Draw 🙃"
#     elif computer_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif user_score == 0:
#         return "Win with a Blackjack 😎"
#     elif user_score > 21:
#         return "You went over. You lose 😭"
#     elif computer_score > 21:
#         return "Opponent went over. You win 😁"
#     elif user_score > computer_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"
#
#
# def play_game():
#
#     # Hint 5: Deal the user and computer 2 cards each using deal_card()
#     user_cards = []
#     computer_cards = []
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
#     # repeated until the game ends.
#
#     while not is_game_over:
#         # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is
#         # over 21, then the game ends.
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"   Your cards: {user_cards}, current score: {user_score}")
#         print(f"   Computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes,
#             # then use the deal_card() function to add another card to the user_cards List. If no, then the game has
#             # ended.
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as
#     # long as it has a score less than 17.
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#
#     print(f"   Your final hand: {user_cards}, final score: {user_score}")
#     print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))
#
#
# # Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# # of blackjack and show the logo from art.py.
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     play_game()


# """ Recall from the solved code"""
# import random
#
#
# def deal_card():
#     """choosing a card form the deck"""
#     card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(card_list)
#     return card
#
#
# def calculate_score(cards):
#     if 11 in cards and sum(cards) == 21:
#         return 0
#     return sum(cards)
#
#
# def compare_score(user_score, computer_score):
#     pass
#
#
# def pay_game():
#     print(deal_card())
#
#
# pay_game()


you_got = 200000
I_got = 1

for _ in range(30):
    you_got += 200000
    I_got += I_got * 2

print(f"You got: {you_got} tk and I got: {I_got} tk")
