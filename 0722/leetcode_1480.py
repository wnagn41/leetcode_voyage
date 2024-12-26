class Solution(object):
    def runningSum(self, nums):
        ans = []
        n = 0
        for i in nums:
            n = n + i
            ans.append(n)
        return ans
    
solution = Solution()


tiem = solution.runningSum([1,2,3,4])
                 
        
print(tiem)