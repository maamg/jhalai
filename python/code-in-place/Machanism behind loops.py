def main():
    print("Pop Quiz! How many continents are there on Earth?")
    answer = int(input())
    while answer != 7:  # That's means it will iterate till answer = 7 
        print("Not quite, guess again!")
        answer = int(input())
    print("That's right! There are seven continents on Earth!")


if __name__ == '__main__':
    main()
