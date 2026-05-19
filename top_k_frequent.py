from collections import Counter


def top_k_frequent(nums, k):
    frequency = Counter(nums)

    sorted_items = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    result = []

    for number, count in sorted_items[:k]:
        result.append(number)

    return result


numbers = [1, 1, 1, 2, 2, 3]
k = 2

print("Top K Frequent Elements:")
print(top_k_frequent(numbers, k))
