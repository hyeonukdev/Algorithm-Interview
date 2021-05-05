# 세수의 합
# input
# nums = [-1, 0, 1, 2, -1, -4]

def threesum(nums):
    results = []
    nums.sort()

    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1 , len(nums)-1
        print("left: {}".format(left))
        print("right: {}".format(right))
        while left < right :
            print("nums[i]: {}".format(nums[i]))
            print("nums[left]: {}".format(nums[left]))
            print("nums[right]: {}".format(nums[right]))
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right += 1
            else:
                results.append((nums[i], nums[left], nums[right]))

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    print("results: {}".format(results))
    return results


nums = [-1, 0, 1, 2, -1, -4]
# print(threesum(nums))
threesum(nums)