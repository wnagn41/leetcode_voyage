class Solution(object):
    def longestValidParentheses(self, s):
        stack = []
        for i in s:
            stack.push(i)
        print(stack)




solution = Solution()

tiem = solution.longestValidParentheses("neweads")

## 再循环中如何正确使用pass continue break

## 如何自由控制输出内容后的换行

print(tiem)