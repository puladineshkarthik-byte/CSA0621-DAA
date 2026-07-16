def binary(arr, l, r, key):
    if l <= r:
        m = (l + r) // 2
        if arr[m] == key:
            return m
        elif arr[m] > key:
            return binary(arr, l, m - 1, key)
        else:
            return binary(arr, m + 1, r, key)
    return -1

arr = [5, 10, 15, 20, 25]
key = 20

result = binary(arr, 0, len(arr) - 1, key)

if result != -1:
    print("Key found at index", result)
else:
    print("Key not found")
