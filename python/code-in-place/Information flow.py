def add_five(x):
    x +=5
    return x


def add_five_buggy(x):
    x += 5


def main():
    x = 10
    add_five_buggy(x)
    print(f"add_five_buggy(): {x}")
    x = add_five(x)
    print(f"add_five(): {x}")



# def main():
#     balance = int(input("Enter initial amount of balance: "))
#     while True:
#         amount = int(input("How much do you want to deposit: "))
#         if amount == 0:
#             break
#         else:
#             deposit(amount)
#             # balance = deposit(amount, balance)
#             print(balance)
#
#
# def deposit(amount, balance):
#     balance += amount
#     return balance


if __name__ == "__main__":
    main()
