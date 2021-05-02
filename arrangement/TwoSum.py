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