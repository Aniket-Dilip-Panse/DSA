# Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.
def doUnion(a,n,b,m):
        return len(set(a) | set(b))