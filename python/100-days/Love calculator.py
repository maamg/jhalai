# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pair_name = name2 + name1
name = pair_name.lower()

true = name.count("t") + name.count("r") + name.count("u") + name.count("e")
love = name.count("l") + name.count("o") + name.count("v") + name.count("e")

score = int(str(true) + str(love))

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score < 40) and (score > 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")