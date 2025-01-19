
def twoSum(nums, target):
    ans = []
    for num in nums:
        for y in nums:
            if nums.index(y) == nums.index(num):
                continue
            else:
                if num + y == target:
                    ans.append(nums.index(num))
                    ans.append(nums.index(y))
                    print(ans)

twoSum([2, 7], 9)
        