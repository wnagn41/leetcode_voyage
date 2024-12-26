class Solution(object):
    def convertTemperature(self, celsius):
        a=[]
        a.append(float(format(celsius + 273.15, ".5f")))
        a.append(float(format(celsius * 1.80 + 32.00, ".5f")))
        return(a)
        
    
solution = Solution()


tiem = solution.convertTemperature(36.50)


## 知识点 ：答案要求的是double 需要知道为什么float()可以创建一个double
print(tiem)