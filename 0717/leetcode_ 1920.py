class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mid_list= []
        final_list= []
        for i in nums:
            mid_list.append(nums[i])

        # print(nums)
        # print(mid_list)
        
        # for j in mid_list:
        #     final_list.append(nums[mid_list[j]])
                              
        return(mid_list)



really_easycompleted reapidly

solution = Solution()


tiem = solution.buildArray([5,0,1,2,3,4])

# 根据返回值 is_valid 进行处理
print(tiem)