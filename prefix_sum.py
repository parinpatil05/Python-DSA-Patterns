def prefix_sum(arr):
    prefix = [0] * len(arr)

    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


numbers = [1, 2, 3, 4, 5]

print("Prefix Sum Array:")
print(prefix_sum(numbers))
