def main():
    # TODO write your solution here
    print("Enter a sequence of non-decreasing numbers.")
    num1 = float(input("Enter num: "))
    num2 = float(input("Enter num: "))
    counting = 1
    while num1 <= num2:
        num1 = num2
        num2 = float(input("Enter num: "))
        counting += 1

    print("Thanks for playing!")
    print("Sequence length: ", counting)


if __name__ == "__main__":
    main()