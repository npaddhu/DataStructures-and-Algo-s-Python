"""Python’s random module includes a function shuﬄe(data) that accepts a list of elements and randomly reorders the
elements so that each possible order occurs with equal probability. The random module includes a more basic function
randint(a, b) that returns a uniformly random integer from a to b (including both endpoints). Using only the randint
function, implement your own version of the shuﬄe function. """

import random
def user_defined_shuffle(data):
    minimum, maximux = min(data), max(data)
    shuffle_data = []
    for i in range(len(data)):
        shuffle_data.append(random.randint(minimum, maximux))

    return shuffle_data

if __name__ == '__main__':

    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(data1)
    print('Built-in shuffle: ', data1)
    print('User defined shuffle: ', user_defined_shuffle(data2))


