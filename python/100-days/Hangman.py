import random
from hangman_art import logo, stages

word_list = ["Ace", "Act", "Age", "Aid", "Aim", "Air", "All", "Arm", "Art", "Ash", "Awe", "Bad", "Bag", "Bar", "Bed", "Bee", "Beg", "Bet", "Bid", "Big", "Bin", "Bit", "Box", "Boy", "Bug", "Bus", "Buy", "Cap", "Car", "Cat", "Cup", "Cut", "Day", "Den", "Die", "Dog", "Dry", "Dub", "Due", "Dug", "Egg", "Eel", "Eve", "Eye", "Fan", "Far", "Fat", "Few", "Fit", "Fly", "Fog", "For", "Fry", "Fun", "Fur", "Gap", "Gas", "Gel", "Gum", "Gun", "Gut", "Guy", "Ham", "Hat", "Hut", "Ice", "Ill", "Ink", "Inn", "Ivy", "Jam", "Jar", "Jet", "Job", "Jog", "Joy", "Key", "Kid", "Kit", "Lab", "Lap", "Law", "Leg", "Lid", "Lie", "Lip", "Log", "Lot", "Map", "Mat", "Max", "May", "Men", "Mil", "Mob", "Mug", "Nap", "Net", "New", "Nun", "Oil", "Old", "Owe", "Own", "Pad", "Pan", "Par", "Pen", "Pet", "Pie", "Pin", "Pit", "Pod", "Pot", "Pub", "Pun", "Put", "Quit", "Rat", "Raw", "Red", "Rib", "Rid", "Rig", "Rim", "Rip", "Rob", "Rot", "Row", "Rub", "Rug", "Sad", "Sat", "Sea", "Sec", "See", "Set", "Sew", "Sex", "She", "Shy", "Sip", "Sit", "Sky", "Sly", "Sob", "Son", "Sow", "Soy", "Spy", "Sub", "Sue", "Sun", "Tab", "Tag", "Tax", "Tee", "Ten", "Tie", "Tin", "Tip", "Toe", "Ton", "Top", "Tow", "Toy", "Try", "Tug", "Tun", "Two", "Vat", "Vet", "Vow", "Wad", "War", "Wax", "Way", "Web", "Wet", "Wig", "Win", "Wit", "Wok", "Yak", "Yam", "Yap", "Yaw", "Yen", "Yes", "Yet", "Yew", "Yin", "Zip", "Crow"]

chosen_word = random.choice(word_list)
chosen_word = chosen_word.lower()
print(logo)

display = []
level = 0
for _ in range(len(chosen_word)):
    display.append("_")

# TODO
while display.count("_") > 0:
    print(display)
    guess = input("Guess a letter: ").lower()
    guess = guess[0]

    if guess in chosen_word:
        matched_letter_count = chosen_word.count(guess)
        for _ in range(matched_letter_count):
            display[chosen_word.index(guess)] = guess
            chosen_word2 = chosen_word.replace(guess, '_', 1)
        print(" ".join(display).capitalize())
        if display.count("_") == 0:
            print("\n Hurrah!You have won the game! \n")
            break
    else:
        level -= 1
        if level <= -6:
            print(stages[level])
            print("OH No!! The Guy has been hanged! Game Over!!")
            print(f"The Word Was: {chosen_word.capitalize()}")
            break
        print("You've lost one more live and made the man near to be hanged")
        print(stages[level])
        if level == -4:
            print(f"Ok, I'm helping you to suggest a letter: {random.choice(chosen_word)}")
