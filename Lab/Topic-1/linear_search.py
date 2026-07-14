arr = [10, 25, 30, 45, 50]
key = 30

for i in range(len(arr)):
    if arr[i] == key:
        print("Key found at index", i)
        break
else:
    print("Key not found")
