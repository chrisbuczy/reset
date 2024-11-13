def removeDuplicates(nums):
        y = 0
        for num in nums:
            x = nums.index(num)
            if x == len(nums) - 1:
                break
            elif num in nums[x+1::]:
                nums[x] = "_"
                y += 1
            else:
                continue
        
        x = [i if i != "_" else nums.remove(i) for i in nums]
        return nums


print(removeDuplicates([0,0,1,1,1,2,2,2,3,3,3,4,4,4,]))