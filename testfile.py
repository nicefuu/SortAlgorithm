def swap(arr, i, j):
    arr[i] ^= arr[j]
    arr[j] ^= arr[i]
    arr[i] ^= arr[j]
arr=[1,2,5,7,9]
swap(arr,0,3)
print(arr)