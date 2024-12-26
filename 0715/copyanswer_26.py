class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
solution = Solution()


tiem = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

# 根据返回值 is_valid 进行处理
print(tiem)