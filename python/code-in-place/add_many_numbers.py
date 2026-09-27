def add_many_numbers(collection):
    return sum(number for number in collection)


number_list = [1,2,3,4,5,6,7,8]

print(add_many_numbers(number_list))
print(sum(number_list))

print(number for number in number_list)