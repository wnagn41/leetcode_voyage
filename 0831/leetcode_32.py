# class Solution(object):
#     def longestValidParentheses(self, s):
#         stack =[-1]
#         max,len = 0,0
#         for i in s:
#             if i == "(":
#                 stack.append(2)
#             else:
#                 ele = stack.pop()
#                 if ele == 2:
#                     len +=2
#                     max = len if len > max else max                                 
#                 elif ele == -1:
#                     stack=[-1]
#         return max
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stck=[-1] # initialize with a start index
        for i in range(len(s)):
            if s[i] == '(':
                stck.append(i)
            else:
                stck.pop()
                if not stck: # if popped -1, add a new start index
                    stck.append(i)
                else:
                    max_length=max(max_length, i-stck[-1]) # update the length of the valid substring
        return max_length





        

solution = Solution()


tiem = solution.longestValidParentheses("()(()")

              
print(tiem)