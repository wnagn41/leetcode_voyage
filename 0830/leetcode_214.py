class Solution(object):
    def shortestPalindrome(self, s):
        reversed_s=s[::-1]
        for i in range(len(s)):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i]+s
solution = Solution()

tiem = solution.shortestPalindrome("")
              
print(tiem)