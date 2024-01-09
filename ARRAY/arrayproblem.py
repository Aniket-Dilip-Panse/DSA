# write a array problem for sorting and searching the array
import array
arr = array.array('i', [10, 20, 30, 40, 50])
print(arr[::-1])

# maximum and minimun element in the array
import array
arr = array.array('i', [100, 20, 30, 40, 50])
print(min(arr))
print(max(arr))
max = arr[0]
for value in arr:
    if value > max:
        max = value
        value,max = max,value
print(max)
print(value)
print(arr)