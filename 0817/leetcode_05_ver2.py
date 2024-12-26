class Solution(object):
    def longestPalindrome(self, s):
        max = 0
        max_str = ""        
        for i in range(len(s)):
            left = i
            right_e = i+2

            while left >= 0 and right_e-1 < len(s):
                if s[left]==s[right_e-1]:
                    if len(s[left:right_e]) > max:
                        max = len(s[left:right_e])
                        max_str = s[left:right_e]
                else:
                    break
                left -=1
                right_e +=1        
        
        for i in range(0,len(s)):
            left = i
            right_o = i+1

            while left >= 0 and right_o-1 < len(s):
                if s[left]==s[right_o-1]:
                    if len(s[left:right_o]) > max:
                        max = len(s[left:right_o])
                        max_str = s[left:right_o]
                else:
                    break
                left -=1
                right_o +=1
        
        return(max_str)


solution = Solution()

tiem = solution.longestPalindrome(" abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa")
              
print(tiem)