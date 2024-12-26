class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))  




## 这里最核心的想法是 本质上 所有的数字10进制都可以用 用9个或者9个以下的数字表示
## 比如

solution = Solution()


tiem = solution.minPartitions("27346209830709182346")

# 根据返回值 is_valid 进行处理
print(tiem)