# Write your code below this line 👇
def prime_checker(number):
    isPrime = True
    for i in range(2, number):
        if number % i == 0:
            isPrime = False
    if isPrime:
        return ("This is a prime number.")
    else:
        return ("This is not a prime number.")


# n = int(input("Check this number: "))
# prime_checker(number=n)
count = 0
for i in range(2, 500):
    if prime_checker(i) == "This is a prime number.":
        print(i)
        count += 1
print(count)

