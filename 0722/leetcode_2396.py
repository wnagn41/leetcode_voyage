class Solution(object):
    def isStrictlyPalindromic(self, n):
        for i in range(2,n-2):
            binary_number=[]
            result = n
            while result != 1:
                binary_number.append(result%i)
                result = result//i
            
            binary_number.append(1)

            return self.par(binary_number)
            return True


    def par(self,binary_number):

        for i in range(len(binary_number)):
            if binary_number[i] == binary_number[len(binary_number)-i-1]:
                pass
            else:
                return False



solution = Solution()


tiem = solution.isStrictlyPalindromic(100)
# 知识点： python转出来的 2禁止数字会产生 一个ob的前缀要冲过list[2:]从第三位开始取
# 知识点: 使用list()将数字转换成list时 产生的list会是一个个分割的数字
                 
        
print(tiem)