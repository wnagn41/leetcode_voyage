class Solution(object):
    def removeElement(self, nums, val):
        nums_res = ['_' for _ in range(len(nums))]
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1

        print(nums_res)
        nums = nums_res
        return j

        

solution = Solution()


tiem = solution.removeElement([0,1,2,2,3,0,4,2],2)

              
print(tiem)