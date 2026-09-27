# # Exercise 1
# # Convert the following variables to different data types and print their types.
#
# num_str = "25"
# num_int = 50
# float_num = 3.14
#
# # Your code here
# str_int = int(num_str)
# int2str= str(num_int)
# float2int = int(float_num)
# print(f"{str_int} is a data type of {type(str_int)}")
# print(f"{int2str} is a data type of {type(int2str)}")
# print(f"{float2int} is a data type of {type(float2int)}")

# Exercise 2
# Perform the following string manipulations and print the results.

# original_string = "Hello, World!"
#
# # Convert the string to uppercase.
# # Replace "Hello" with "Hi".
# # Split the string into a list of words.
#
# # Your code here
# string_uppercase = original_string.upper()
# replace_Hello = original_string.replace("Hello", "Hi")
# split_str = original_string.split()
# print(split_str)

# name = 'abdul aziz'
# letters_in_my_name = [letter for letter in name if letter.isalpha()]
# print(letters_in_my_name)

#
# # Exercise 3
# # Perform the following operations on the given list and print the results.
#
# my_list = [1, 2, 3, 4, 5]
#
# # Append the number 6 to the list.
# # Remove the element 3 from the list.
# # Access and print the element at index 2.
#
# # Your code here
# append_6 = my_list.append(6)
# remove_3 = my_list.remove(3)
# print(my_list[2])

# # Exercise 4
# # Try to modify the elements of the tuple, and observe the result.
#
# my_tuple = (1, 2, 3, 4)
#
# # Attempt to change the value at index 1 to 10.
#
# # Your code here
# 'In python tuple is not mutable'


# Exercise 5
# Evaluate the following boolean expressions and print the results.

x = True
y = False

# Check if x is True and y is False.
# Check if x is True or y is True.
# Check if not x is True.

# Your code here
if x is True and y is False:
    print("Yes, x is True and y is False")
if x is True or y is True:
    print("Yes,X is True or Y is True")
if x is not True:
    print("X is not True")
else:
    print("No, X is True ")