# # Write a Python program to count the number of items in a dictionary that have a value greater than a certain number.
# def count_items_above_value(my_dict, value):
#     count = 0
#     for item in my_dict.values():
#         if item > value:
#             count += 1
#     return count
# my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# value = 25
# count = count_items_above_value(my_dict, value)
# print(count)

# # This program defines a function called count_items_above_value that takes two arguments: my_dict is the dictionary to be searched, and value is the number to compare each item against.
# #  The function initializes a counter variable count to zero, and then iterates over the values of the dictionary using the .values() method.
# #  For each value, it checks if it is greater than the specified value and, if so, increments the count variable.

# # To use this function with a dictionary, simply call it and pass in the dictionary and the comparison value as arguments:
# # In this example, the dictionary my_dict has four items, two of which have values greater than value=25.
# #  The program will therefore output 2, indicating that two items in the dictionary meet the comparison criteria.
# my_dicts ={"mango":5,"apple":3,"orange":7,"banana":8}
# value = 5
# count = len([x for x in my_dicts.values()if x< value])
# print(count)

#Write a function that takes a list of numbers as input and returns a new list with all duplicate numbers removed.
def input(duplicate):
    empty=set(duplicate)
    return list(empty)
duplicate = [2,2,5,6,7,8,5,4,77,2]
# dupli = input(list(duplicate))
print(input(list(duplicate)))


    