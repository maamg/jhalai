import random


def main():
    print("Khansole Academy")
    # TODO: your code here
    # randomly generating 2 numbers
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    sum12 = num1 + num2
    print(f"What is {num1} + {num2}?")

    # User input
    answer = int(input(f"Your answer: "))

    # input assessment
    if sum12 == answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {sum12}")


if __name__ == '__main__':
    main()
