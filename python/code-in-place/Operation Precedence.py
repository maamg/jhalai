def main():
    a = True
    b = False
    c = False
    d = True

    # Option 1
    if (a and not b) and (b or (d and a)):
        print("Option 1 is True!")

    # Option 2
    if a and (b or (d and not (not c or (a and d and c)))):
        print("Option 2 is True!")

    # Option 3
    if (a and not b and not c and d and (a and d) and not (b or c)) and not (d and (a or (b and c)) and c):
        print("Option 3 is True!")


if __name__ == "__main__":
    main()
