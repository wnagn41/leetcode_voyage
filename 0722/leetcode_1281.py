class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0 
        mul = 1
        a = str(n)
        for i in a:
            i = int(i)
            sum += i
            mul *=i
        return(mul-sum)

solution = Solution()


tiem = solution.subtractProductAndSum(234)
## 从摩尔到第一位，通过求余的方式得到末位 并进行操作     




    #   class Solution(object):
    # def subtractProductAndSum(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     s = 0
    #     prod = 1
    #     while n:
    #         a = n%10
    #         s += a
    #         prod *= a
    #         n = n/10
    #     return prod - s
              
print(tiem)