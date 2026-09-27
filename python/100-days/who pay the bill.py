# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_number = len(names)
payer_index = random.randint(0, names_number-1)
print(f"{names[payer_index]} is going to buy the meal today!")