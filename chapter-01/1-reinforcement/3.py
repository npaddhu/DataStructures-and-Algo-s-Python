"""Write a short Python function, minmax(data), that takes a sequence of one or more numbers, and returns the
smallest and largest numbers, in the form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""


def get_min_max_value(numbers):
    """
    # Solution1: more number of comparisons
    minValue = maxValue = numbers[0]
    for value in numbers[1:]:
        if minValue > value:
            minValue = value
        if maxValue < value:
            maxValue = value
    return (minValue, maxValue)
    """
    # solution2: Less number of comparisons
    if (len(numbers) == 1):
        minValue = maxValue = numbers[0]
        return (minValue, maxValue)
    if numbers[0] < numbers[1]:
        minValue, maxValue = (numbers[0], numbers[1])
    else:
        minValue, maxValue = (numbers[1], numbers[0])

    for value in numbers[2:]:
        if (minValue > value):
            minValue = value
        elif (maxValue < value):
            maxValue = value
    return (minValue, maxValue)


if __name__ == '__main__':
    numbers = [int(input('Enter element: ')) for _ in range(int(input('Enter number of Values:')))]
    minValue, maxValue = get_min_max_value(numbers)
    print("minimum = {0}, maximum = {1}".format(minValue, maxValue))
