""" Python allows negative integers to be used as indices into a sequence, such as a string. If string s has length n,
and expression s[k] is used for index−n≤k<0,what is the equivalent index j≥0 such that s[j] references the same element?
"""

# since k is negative, j = n + k
# Eg;
seq = [1, 2, 3, 4, 5, 6]
n = len(seq)
k = -3
print(seq[k])
print(seq[n + k])







