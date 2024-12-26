class Solution(object):
    def shuffle(self, nums, n):
        len_n = float(len(nums))
        a=[]
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i+n])
        return(a)


solution = Solution()


tiem = solution.shuffle([2,5,1,3,4,7],3)


## 知识点 ：很难对每一次变量变化时 method会如何有一个具体的认识 抄答案了放弃
print(tiem)