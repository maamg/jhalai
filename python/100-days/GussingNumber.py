# Previous implementation
#
# # Number Guessing Game Objectives:
# import random
#
# # Include an ASCII art logo.
# logo = '''
#   __ \               | | | |          | \ | |               | |
# | |  \/_   _ ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __
# | | __| | | / __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
# | |_\ \ |_| \__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |
#  \____/\__,_|___/___/  \__|_| |_|\___| \_| \_/\__,_|_| |_| |_|_.__/ \___|_|'''
#
# print(logo)
# Targeted_number = random.choice(range(101))
# # print(Targeted_number)
# print('''Welcome to the Number Guessing Game!
#
# I'm thinking of a number between 1 and 100.\n''')
# life =0
#
# level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
# if level.lower() == 'easy':
#     life = 10
# elif level.lower() == 'hard':
#     life = 5
#     print(f"You have {life} attempts remaining to guess the number.")
#
# while life > 0:
#     # Allow the player to submit a guess for a number between 1 and 100.
#     guessingNumber = int(input("Make a guess:"))
#     # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
#
#     if guessingNumber < Targeted_number:
#         print("Too low")
#         life = life - 1
#         print(f"You have {life} attempts remaining to guess the number.")
#
#     elif guessingNumber > Targeted_number:
#         print("Too high")
#         life = life -1
#         print(f"You have {life} attempts remaining to guess the number.")
#
#     else:
#         print(f"Yes the Actual Number is {Targeted_number} ")
#         break
#
# if life <1:
#     print("And You loss the game")
import random
def choosing_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': \n")
    if level == 'easy':
        level = 5
    elif level == 'hard':
        level = 10
    return level


def running_game(level):
    target_number = random.randint(50)
    guessing_number = 0
    while level > 0:
        guessing_number = int(input("Guess a number"))
        if guessing_number < target_number:
            print("Too Low")
            guessing_number = int(input("Guess a number"))
            level -= 1
        elif target_number < guessing_number:
            print("Too High")
            guessing_number = int(input("Guess a number"))
            level -= 1
        else:
            print("You've got it")

def game():
    choosing_level()
    running_game()