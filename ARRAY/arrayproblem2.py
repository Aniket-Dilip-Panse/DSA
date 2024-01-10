# finding Maximum and Minimum number from array 
def MaximumNumber(arr):
    max = arr[0]
    for value in arr:
        if max<i:
            max = i
    return max

def MinimumNumber(arr):
    min = arr[0]
    for value in arr:
        if max>i:
            max = i
    return max

print(MaximumNumber([1,3,56,73,182,74]))
print(MinimumNumber([1,3,56,73,182,74]))