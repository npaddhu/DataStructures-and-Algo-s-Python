"""Had we implemented the scale function (page 25) as follows, does it work properly?
def scale(data, factor):
    for val in data:
        val *= factor
Explain why or why not."""

# At page25
def scale1(data, factor):
    for i in range(len(data)):
        data[i] *= factor
    return

# Question
def scale(data, factor):
    """data will not not change, bcoz we are multiplying val individually but not adding to the list"""
    for val in data:
        val *= factor

if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    print(data)
    scale(data, factor=2)
    print(data)

