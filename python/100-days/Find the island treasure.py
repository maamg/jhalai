print(
'''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

for _ in range(6):
    print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
    Input = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''')

    if Input.lower() == "left":
        Input2 = input(
            '''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to swim across.\n''')
        if Input2.lower() == "wait":
            Input3 = input(
                "You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one "
                "blue. Which color do you choose?\n")
            if Input3.lower() == "yellow":
                print("You Win")
            else:
                print("Game Over")
        else:
            print("Game Over")
    else:
        print("Game Over")

# Different way:

# if Input.lower() == 'right':
#     print("Game Over")
#
# elif Input.lower() == "left":
#     Input2 = input('''You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "Swim" to swim across.''')
#     if Input2.lower() == "swim":
#         print("Game Over")
#
#     elif Input2.lower() == "wait":
#         Input3 = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one "
#                        "blue. Which color do you choose?")
#         if Input3.lower() == "blue":
#             print("You Won")
#         else:
#             print("Game Over")

