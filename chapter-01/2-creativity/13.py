""" Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in
the opposite order than they were before, and compare this method to an equivalent Python function for doing the same
thing. """

# Method1
def reverse_list1(numbers):
    reverse_list = []
    for item in numbers:
        reverse_list.insert(0, item)
    return reverse_list

# Method2
def reverse_list2(numbers):
    if len(numbers) == 1:
        return numbers

    return reverse_list2(numbers[1:]) + [numbers[0]]

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print("Original list: ", numbers)
    print("Reversed list By Method1: ", reverse_list1(numbers))
    print("Reversed list By Method2: ", reverse_list2(numbers))
