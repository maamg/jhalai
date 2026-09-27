import math

# The constant K in the half life formula
K = -8266.64258429376


def main():
    while True:
        calculate_age_single_sample()


def calculate_age_single_sample():
    # ask the user to enter the percentage c14 left in their sample
    pct_left = float(input("% of natura c14 in your sample: "))
    age = K * math.log(pct_left/100)
    # print the result
    print("Sample is " + str(age) + " years old")


# tells python to call main when the program starts
if __name__ == '__main__':
    main()

