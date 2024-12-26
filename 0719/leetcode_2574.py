class Solution(object):
	def leftRightDifference(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		left_max=[]
		right_max=[]
		len_nums=len(nums)
		for i in range(len_nums):
			left = 0
			while i < len_nums:
				left = left + nums[i]
				i = i+1
			right_max.append(left)
			
					
					
		print(right_max,left_max)


solution = Solution()


tiem = solution.leftRightDifference([10,4,8,3])


## 知识点 ：很难对每一次变量变化时 method会如何有一个具体的认识 抄答案了放弃  

不行 无论如何要好好想想
print(tiem)