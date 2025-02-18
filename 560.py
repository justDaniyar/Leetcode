
def subarraySum(nums, k):
    prefix = [0 for i in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]

    return prefix

# print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
