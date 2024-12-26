
class Solution(object):
    def numIdenticalPairs(self, nums):
        a=0
        for i in range(len(nums)):
            this_num = nums[i]
            for j in range(i+1,len(nums)):
                if this_num == nums[j]:
                    print(this_num)
                    a += 1
        return (a)
solution = Solution()


tiem = solution.numIdenticalPairs([1,2,3,1,1,3])


# 知识点 ： 这段代码适用于所有 将数列中的数字进行22比较的操作       
#         for i in range(len(nums)):
#             this_num = nums[i]
#             for j in range(i+1,len(nums)):
                 
        
print(tiem)