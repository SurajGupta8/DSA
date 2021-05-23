
# Pairs:

# Given an array ar[] containing N integers, and an integer S denoting target sum.

# Find two distinct integers from the array s.t. they can pair up to form the target sum.

# Input:
# ar = [10, 5, 2, 3, -6, 9, 11]
# S = 4

# Output:
# [10, -6]


from sys import stdin, stdout
if __name__ == '__main__':
    ar = [int(x) for x in stdin.readline().split()]
    sm = int(stdin.readline())
    s = set()
    for i in ar:
        x = sm - i
        if x in s:
            l = [i, x]
            print(l)
            s.add(i)
        else:
            s.add(i)
