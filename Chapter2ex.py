
# INSERTION SORT

A = [100,41, 59, 26, 41, 58, 87, 2]  # This is a list

def insertion_sort(A):
    i = 0
    j = 0
    for j in range(1,len(A)):
        key = A[j]
        ## Insert element into sorted sequence
        i = j - 1
        while (i >= 0 and A[i] > key):
            A[i+1] = A[i]
            A[i] = key
            i = i - 1
        A[i+1] = key # leave key as key
        print(j)
    return(A)

def insertion_sort2(A):
    for j in range(1,len(A)):
        key = A[j]
        ## Insert element into sorted sequence
        i = j - 1
        while (i >= 0 and A[i] < key):
            A[i+1] = A[i]
            A[i] = key
            i = i - 1
        A[i+1] = key # leave key as key
        print(j)
    return(A)


C = [1, 25, 34, 66, 11, 28, 99, 100]
d = 11

def linear_search(B,v):

    """

    :rtype: int
    """
    for i in range(len(B)):
        if B[i] == v:
            print(B[i])
            return i

    return 0

print(linear_search(C,d))



