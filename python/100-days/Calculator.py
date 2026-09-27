# Calculator Application

# Add
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiple(a, b):
    return a * b


# Division
def divide(a, b):
    return a / b


# Calculation dictionary

operations = {
    '+': add,
    '-': subtract,
    '*': multiple,
    '/': divide
}


def calculator():
    num1 = float(input("Press the first number to calculate: "))
    for symbol in operations:
        print(symbol)
    continueCalculating = True

    while continueCalculating:
        operation = input("Press any of the calculation operation from the above: ")
        num2 = float(input("Press another number to calculate: "))
        calculation_function = operations[operation]
        result = calculation_function(num1, num2)
        print(f" {num1} {operation} {num2} = {result}")
        if input(f"Do you want to calculate with {result} ? if yes type y, else type n: ")== 'y':
            num1 = result
        else:
            continueCalculating = False
            calculator()


calculator()
