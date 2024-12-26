class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) is 1 or len(nums) is 0:
            return False
        for i in range(len(nums)):
            print(nums[i],nums[0:i])
            if nums[i] in nums[0:i]:
                return True
        return False

        

solution = Solution()

tiem = solution.containsDuplicate([1,2,3,1])
           
print(tiem)