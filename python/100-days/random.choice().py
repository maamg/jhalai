import random

NumberList = ["one", "two", "twelve", "five", "four", "seven", "nine"]
print(NumberList)

for _ in range(9):
    print(random.choice(NumberList))
