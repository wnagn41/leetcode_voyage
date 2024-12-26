class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        return [sorted(nums).index(i) for i in nums]

solution = Solution()


tiem = solution.smallerNumbersThanCurrent([8,1,2,2,3])
## reversed_list = input_list[::-1]           
        
print(tiem)