# https://www.geeksforgeeks.org/top-50-array-coding-problems-for-interviews/
# Find a peak element which is not smaller than its neighbours
import array
arr = array.array('i', [ 1, 3, 20, 4, 1, 0 ])
def find_peak(arr):
    if arr[0]>arr[1] and arr[-1]>arr[-2]:
        return arr[0],arr[-1]
    else:
        for i in range(1,len(arr)-1):
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return arr[i]
        return arr

print(f'The peak element of array is {find_peak(arr)}')