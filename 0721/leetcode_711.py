class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        sta = list(stones)
        jew = list(jewels)
        a = 0
        for i in sta:
            if i in jew:
                a += 1

        return a

solution = Solution()


tiem = solution.numJewelsInStones("aA","aAAbbbb")


## 知识点 ：很难对每一次变量变化时 method会如何有一个具体的认识 抄答案了放弃
print(tiem)