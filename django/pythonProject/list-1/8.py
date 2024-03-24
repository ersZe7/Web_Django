def max_end3(nums):
    max_value = max(nums[0], nums[2])
    return [max_value, max_value, max_value]

print(max_end3([1, 2, 3]))    # Output: [3, 3, 3]
print(max_end3([11, 5, 9]))   # Output: [11, 11, 11]
print(max_end3([2, 11, 3]))   # Output: [3, 3, 3]
