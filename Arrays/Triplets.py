# Triplets

# Given an array ar[] containing N integers, and an integer S denoting target sum.
# Find all distinct integers from the array s.t. they can pair up to form the target sum. The numbers in each triplet should be ordered in ascending order, and triplets should be ordered too.

# Input:
# ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 15]
# S = 18

from sys import stdin, stdout
if __name__ == '__main__':
    
    a = [1,2,3,4,5,6,7,8,9,15]
    t = 18
    
    # sorting array in ascending order...
    a.sort()
    res = []
    n = len(a)
    for i in range(0, n - 2):
        j = i+1
        k = n-1

        # using two pointer aproach for calculating pair sum...
        while(j < k):
            s = 0
            s += a[i]
            s += a[j] 
            s += a[k]
            
            if(s == t):
                res.append([a[i], a[j], a[k]])
                j += 1
                k -= 1
            elif(s > t):
                k -= 1
            else:
                j += 1

    #print(res)
    stdout.write(str(res))
