def product_except_self(nums):
    n = len(nums)

    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


numbers = [1, 2, 3, 4]

print("Product Except Self:")
print(product_except_self(numbers))
