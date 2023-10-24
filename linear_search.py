# Instructions:
# Create a Python function named linear_search that takes two arguments:
#
# input_list: A list of integers.
#
# target: The element you want to find in the list.
#
# Inside the function, initialize a variable index to -1.
# This variable will be used to store the index of the target element if found.
#
# Use a for loop to iterate through the input_list.
# For each element in the list, compare it with the target.
# If they match, update the index variable with the current index and break out of the loop.
#
# After the loop, check the value of the index variable.
# If it is still -1, return -1 to indicate that the element is not in the list.
# Otherwise, return the index as the position of the target element.

def linear_search(my_list: list, target : int) -> int:
    index = -1
    for num in my_list:
        if num == target:
            index = my_list.index(num)
            break
    return index


input_list = [1, 5, 6, 7, 10, 14, 17, 23, 34, 55, 67, 76, 88, 91, 98]
target_input = int(input("Please enter a target real number from 1 to 99:"))
result = linear_search(input_list, target_input)

if result != -1:
    print(f"The target element {target_input} is at index {result}.")
else:
    print(f"The target element {target_input} was not found in the list.")