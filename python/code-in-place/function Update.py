


def main():
    number = int(input("Give some integer: "))
    while number > 1:
        number_series = []
        number_series.append(next_number(number))

    pass


def next_number(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        number /= 2
        return number
    else:
        number = number*3 + 1
        return number



if __name__ == "__main__":
    main()

# def main():
#     number = int(input("Some positive integer: "))
#     number_series = [number]
#     while number > 1:
#         if number % 2 != 0:
#             number = number*3 +1
#             number_series.append(number)
#         else:
#             number = int(number/2)
#             number_series.append(number)
#     print(number_series)
#
#
# if __name__ == "__main__":
#     main()
