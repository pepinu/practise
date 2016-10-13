arr_size = input()
passes = 0
swaps = 0
swapped = True
arr = raw_input().split()
arr = [int(x) for x in arr]
while swapped:
    swapped = False
    passes += 1
    for i in range(arr_size - 1):
        if arr[i] > arr[i + 1]:
            swapped = True
            swaps += 1
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp
print passes, swaps
