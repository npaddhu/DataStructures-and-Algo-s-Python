""" Write a short Python function that takes a positive integer n and returns the sum of the squares of all the
odd positive integers smaller than n. """


def get_sum_of_squares_of_odd_numbers(n):
    sumOfOddValues = 0
    for value in range(n):
        if value % 2 != 0:
            sumOfOddValues += (value * value)
    return sumOfOddValues


if __name__ == '__main__':
    print(get_sum_of_squares_of_odd_numbers(int(input('Enter n value: '))))