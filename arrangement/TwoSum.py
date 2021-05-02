# 두 수의 합
# input
# nums = [2, 7, 11, 15] , target =9
# output
# [0, 1]
# --------------------------------

# 브루트 포스 방식 -> n^2
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [2, 7, 11, 15]
target =9
print(twoSum(nums, target))

# in 탐색
def twoSum_1(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i +1:]:
            return nums.index(n), nums[i +1:].index(complement)+ (i+1)

print(twoSum_1(nums, target))


# 조회 구조 개선
def twoSum_2(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

print(twoSum_2(nums, target))