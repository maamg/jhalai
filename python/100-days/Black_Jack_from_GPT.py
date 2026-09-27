import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    """Deals two cards to the player and two to the computer"""
    player_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)
    return player_cards, computer_cards


def get_card(cards):
    """Returns one card from the deck"""
    return random.choice(cards)


def calculate_score(cards):
    """Calculates the score for a given hand of cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    """Compares the player and computer scores to determine the winner"""
    if player_score == computer_score:
        return "It's a tie!"
    elif computer_score == 0:
        return "Computer has Blackjack. You lose!"
    elif player_score == 0:
        return "You have Blackjack! You win!"
    elif player_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif player_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    """Runs the game"""
    print("Welcome to Blackjack!")
    player_cards, computer_cards = deal_cards()

    while True:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            print(compare(player_score, computer_score))
            break

        while input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_cards.append(get_card(cards))
            player_score = calculate_score(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score == 0 or player_score > 21:
                print(compare(player_score, computer_score))
                break

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(get_card(cards))
            computer_score = calculate_score(computer_cards)

        print(f"Your final hand: {player_cards}, final score: {player_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(player_score, computer_score))
        break


play_game()
