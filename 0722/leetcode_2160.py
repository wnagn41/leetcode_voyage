class Solution(object):
    def minimumSum(self, num):
        a = len(str(num))
        ans = num
        b = []
        for i in range(a): 
            b.append(ans%10)
            ans = ans//10
        b.sort()

        sum = b[0]*10 + b[1]*10 + b[2] + b[3]
        return sum
            

        








solution = Solution()


tiem = solution.minimumSum(2932)
        
print(tiem)