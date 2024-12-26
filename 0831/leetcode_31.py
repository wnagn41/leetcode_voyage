class Solution(object):
    def nextPermutation(self, nums):
        for i in range(len(nums)):
            print(nums[len(nums)-i-1])
            if nums[len(nums)-i-1] < nums[len(nums)-i-2]:
                print(nums[len(nums)-i-1])
            


        

solution = Solution()

tiem = solution.nextPermutation([1,2,3,4,5])
print(tiem)