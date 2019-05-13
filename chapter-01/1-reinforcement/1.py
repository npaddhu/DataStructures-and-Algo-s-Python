'''
R-1.1 Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a multiple of m, that is,n = mi for some integer i, and False otherwise.
'''

def is_multiple(n, m):
    return True if n%m == 0 else False

if __name__=="__main__":
    n = int(input('Enter n value'))
    m = int(input('Enter m value'))
    result = is_multiple(n, m)
    print('n is multiple of m1:', result)