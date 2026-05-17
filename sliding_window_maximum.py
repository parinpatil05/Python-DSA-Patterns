from collections import deque


def max_sliding_window(nums, k):
    queue = deque()
    result = []

    for i in range(len(nums)):

        while queue and queue[0] < i - k + 1:
            queue.popleft()

        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()

        queue.append(i)

        if i >= k - 1:
            result.append(nums[queue[0]])

    return result


numbers = [1, 3, -1, -3, 5, 3, 6, 7]
window_size = 3

print("Maximum in Sliding Window:")
print(max_sliding_window(numbers, window_size))
