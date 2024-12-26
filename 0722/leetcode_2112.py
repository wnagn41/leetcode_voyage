class Solution(object):
    def mostWordsFound(self, sentences):
        a = 0
        max = 0
        for i in sentences:
            num = i.count(" ")
            if num > max:
                max = num

        return max 


solution = Solution()


tiem = solution.mostWordsFound(["alice and bob love leetcode","i ds dfsd dfds fdsf think so too","this is great thanks very much"])
                 
        
print(tiem)