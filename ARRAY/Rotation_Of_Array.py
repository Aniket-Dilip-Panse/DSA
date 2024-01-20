# array rotation in python
# https://www.geeksforgeeks.org/array-rotation/
# 1)right array rotation 
# 2)left array rotation 
# 3)rotate one by one
# 4)using temporary array
# 5)Juggling algorithm
# 6)Reversal algorithm

# 1)Right Rotation:- 
# input array: 1 2 3 4 5
# output array: 5 1 2 3 4

def rightRotation(arr,shift):
    # step:-1 Store the first element of the array in a temporary variable.
    # d = shifting of array element
    for i in range(0,shift):
        temp = arr[-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] = temp
    return arr
print(rightRotation([1,2,3,4,5],2))
