import random

lose = '''
      

            ||||||||||||||
           =              \       ,
           =               |
          _=            ___/
         / _\           (o)\
        | | \            _  \
        | |/            (____)
         \__/          /   |
          /           /  ___)
         /    \       \    _)                       )
        \      \           /                       (
      \/ \      \_________/   |\_________________,_ )
       \/ \      /            |     ==== _______)__)
        \/ \    /           __/___  ====_/
         \/ \  /           (O____)\\_(_/
                          (O_ ____)
                           (O____)

by tod@m-net.arbornet.org


 '''
win = '''
            .
          ,i \
        ,' 8b \
      ,;o  `8b \
     ;  Y8. d8  \
    -+._ 8: d8. i:
        `:8 `8i `8
          `._Y8  8:  ___
             `'---Yjdp  "8m._
                  ,"' _,o9   `m._
                  | o8P"   _.8d8P`-._
                  :8'   _oodP"   ,dP'`-._
                   `: dd8P'   ,odP'  do8'`.
                     `-'   ,o8P'  ,o8P' ,8P`.
                       `._dP'   ddP'  ,8P' ,..
                          "`._ PP'  ,8P' _d8'L..__
                              `"-._88'  .PP,'7 ,8.`-.._
                                   ``'"--"'  | d8' :8i `i.
                                             l d8  d8  dP/
                                              \`' J8' `P'
                                               \ ,8F  87
                                               `.88  ,'
                                                `.,-' mh
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

your_point = 0
computer_point = 0
for _ in range(3):
    computer_choice = random.randint(0, 2)

    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    print("your chose:")

    if your_choice == 0:
        print(rock)
    elif your_choice == 1:
        print(paper)
    elif your_choice == 2:
        print(scissors)

    print("Computer Chose:")
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    if computer_choice == 0 and your_choice == 1:
        print("You Win")
        your_point +=1
    elif computer_choice == 0 and your_choice == 2:
        print("You Lose")
        computer_point += 1
    elif computer_choice == 1 and your_choice == 0:
        print("You Lose")
        computer_point += 1
    elif computer_choice == 1 and your_choice == 2:
        print("You Win")
        your_point +=1
    elif computer_choice == 2 and your_choice == 0:
        print("You Win")
        your_point += 1
    elif computer_choice == 2 and your_choice == 1:
        print("You Lose")
        computer_point += 1
    else:
        print("It's a draw")

if your_point > computer_point :
    print("জিতছো মিয়া! নাও চকলেট খাও:")
    print(win)

else:
    print("হারছোস ব্যাটা! গুলি খা! ঢিশকাউ! ")
    print(lose)