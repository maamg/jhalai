import random
from hangman_art import logo, stages

# TODO-1: FIRST GENERATING A EASILY PICKABLE WORD LIST
print(logo)
word_list = ["actor", "area", "answer", "arm", "article", "bank", "beach", "bean", "bed", "bag", "bend", "bread", "bus",
             "cake", "candle", "carrot", "cat", "chip", "clock", "cloth", "club", "cow", "crop", "cover", "cup",
             "cycle", "day", "dish", "doctor", "dog", "door", "egg", "eye", "fan", "farm", "fun", "field", "film",
             "fire", "fish", "flood", "floor", "food", "fort", "frog", "fruit", "game", "gift", "glass", "glue",
             "grain", "grape", "hand", "hanger", "hat", "head", "hen", "home", "host", "hut", "ice", "island", "jar",
             "jeep", "job", "juice", "knee", "land", "letter", "light", "lion", "love", "magazine", "man", "math",
             "meat", "milk", "money", "mouth", "mud", "music", "nation", "nap", "nest", "night", "nut", "nod", "oil",
             "office", "paint", "panic", "park", "pen", "people", "phone", "place", "poem", "pay", "rabbit", "rain",
             "rat", "tattle", "rice", "river", "road", "roof", "rule", "nose", "school", "scissor", "sea", "sell",
             "shoe", "shirt", "sign", "sky", "smile", "smoke", "song", "sound", "spot", "storm", "story", "sun",
             "study", "sweet", "swim", "tea", "teacher", "teeth", "temple", "tent", "tie", "tiger", "torch", "tourist",
             "town", "toy", "train", "tree", "true", "van", "valley", "voice", "water", "wind", "women", "yard", "zoo"]
print(len(word_list))
# TODO-2: RANDOM.CHOICE A WORD & GENERATE A BLANK STRING
chosen_word = random.choice(word_list)
print(chosen_word)
blank = []
for _ in chosen_word:
    blank.append('_')

# TODO-3: USER INPUT FOR A GUESS LETTER WHILE BLANK REMAINS
while blank.count('-') != 0:

    guess = input("Guess a letter and fill the blank: ")

    # TODO-4: CHECKING THE LETTER AND FILL  THE BLANK OR COUNT THE WRONG TRY

    if guess in chosen_word:
        for _ in chosen_word.count(guess):

        blank[chosen_word.index(guess)] = guess

    print(stages[-1])
    # TODO-5: WINING THE GAME IF FILLS ALL THE BLANK OR GAME OVER IF TRYS OVER
