class Solution(object):
    def search(self, nums, target):
        if len(nums) ==1:
            if nums[0] == target:
                return target
            else:
                return -1
        low,high = 0, len(nums)-1
        mid = (high + low) // 2

        while nums[mid] != target:
            if high < low:
                return -1
            if nums[mid] > target:
                high = mid -1
            else:
                low = mid + 1
            mid = (high+low) // 2
        
        return mid
        



        

solution = Solution()


tiem = solution.search([-1,0,3,5,9,12],2)

              
print(tiem)