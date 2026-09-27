# # Problem: Beginner Level
# # Write a Python function that takes two integers as input and returns their sum.
#
# def sum2int(int1, int2):
#     return int1 + int2

# # Exercise 2: Intermediate Level
# # Problem:
# # Given a list of integers, write a Python function that returns the sum of all even numbers in the list.
#
# def sum_even_num(num_list):
#     result = 0
#     for num in num_list:
#         if num % 2 == 0:
#             result += num
#     return result
#
#
# result = sum_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(result)


# # Exercise 3:
# # Intermediate Level Problem: Write a Python program that reads a text file and counts the occurrences of
# # each word. Print the word frequencies in descending order.
#
# file = open('file.txt', 'r')
#
#
# def count_word(file_):
#     word_count = 0
#     for line in file_:
#         word_count += len(line.split())
#     return word_count
#
#
# words = count_word(file)
# print(words)


# def count_word_occurrences(file_path):
#     word_count = {}
#
#     with open(file_path, 'r') as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 # Remove punctuation and convert to lowercase for better counting
#                 cleaned_word = word.strip('.,?!()[]{}"\'').lower()
#
#                 if cleaned_word:
#                     print()
#                     word_count[cleaned_word] = word_count.get(cleaned_word, 0) + 1
#
#     return word_count
#
#
# file_path = 'file.txt'
# word_occurrences = count_word_occurrences(file_path)
#
# # Print word frequencies in descending order
# for word, count in sorted(word_occurrences.items(), key=lambda x: x[1], reverse=True):
#     print(f'{word}: {count}')


fruit_list = ["apple", "orange", "banana", "apple", "banana", "orange", "apple", "grape"]

# def fruits_count(fruits):
#     fruit_count = {}
#     for fruit in fruits:
#         fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
#         # fruit_count["apple"] = fruit_count.get("apple", 0) + 1 = 0 '''fruit_count= {"apple" :0} + 1 = 0 +1 '''
#
#     return fruit_count
#
#
# print(fruits_count(fruit_list))


# def calculate_total_expenses(ex_list):
#     total_expense = 0
#     for item in ex_list:
#         total_expense += item[1]
#     return total_expense
#
#
# expenses_list = [("groceries", 50), ("dinner", 30), ("gas", 20), ("coffee", 5)]
# total_spent = calculate_total_expenses(expenses_list)
# print(f"Total amount spent: ${total_spent}")


def calculate_income_expenses(transaction_detail):
    trans_dic = {}
    total_income = 0
    total_expense = 0
    for item in transaction_detail:
        if item[0].lower() == 'income':
            total_income += item[1]
        elif item[0].lower() == 'expense':
            total_expense += item[1]
    trans_dic['income'] = trans_dic.get('income', total_income)
    trans_dic['expenses'] = trans_dic.get('expenses', total_expense)
    # trans_dic['income'] = total_income
    # trans_dic['expenses'] = total_expense
    return trans_dic


transactions_list = [("income", 1000), ("expense", 50), ("expense", 30), ("income", 500)]
result = calculate_income_expenses(transactions_list)
print(f"Total income: ${result['income']}")
print(f"Total expenses: ${result['expenses']}")