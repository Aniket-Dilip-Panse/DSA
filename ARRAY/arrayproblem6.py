# Given a sorted array arr[] and a number x, write a function that counts the occurrences of x in arr[]. Expected time complexity is O(Logn) 
def valueCount(arr,n,x):
    count = 0
    for value in range(0,n):
        if arr[value] == x:
            count = count + 1
        else:
            pass
    return count
print(valueCount([1, 1, 2, 2, 2, 2, 3],7,2))