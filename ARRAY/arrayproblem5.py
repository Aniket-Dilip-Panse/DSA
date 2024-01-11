# Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Note :-  l and r denotes the starting and ending index of the array.
def kthSmallest(arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]
kthSmallest([5,3,5,6,2,6,2],0,len(arr-1),3)