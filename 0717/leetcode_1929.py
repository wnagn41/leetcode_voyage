class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = nums[:]
        for i in nums:
            list.append(i)
        return list
    
solution = Solution()


tiem = solution.getConcatenation([3,9,20,15,7])


## 知识点 ： copy 和 deep copy的区别 如何用a给b赋值 但是 在修改a的时候 b不会发生相应的改变
## 2 选择文本后 点击comd+d 复选下一个一样的文本 然后就可以批量修改了
# 根据返回值 is_valid 进行处理
print(tiem)