class Solution(object):
    def divide(self, nums, val):
        print ("n:",nums,"\ndiv:", val)
        reminder = abs(nums)
        val_t = abs(val)
        i = 0
        if nums == 0:
            return 0 
        while reminder >= 0:
            reminder = reminder - val_t
            i += 1
        if nums ^ val >= 0:
            return i-1
        else:
            return 1-i
        



        

solution = Solution()


tiem = solution.divide(20,-6)

              
print(tiem)