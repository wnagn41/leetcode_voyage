class Solution(object):
    def isValid(self, s):
        stack = [] # only use append and pop
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)

            elif len(stack) == 0:
                return False            
            elif bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0


##作业小总结 因为有可能对数据进行操作 比如这个pop对stack惊醒了读取和减少两个操作，所以一定要注意判断条件的顺序
##因为条件可能修改了数据

##这个是错的
##t = Solution('()')
##Solution.isValid(t)

# 实例化 Solution 类
solution = Solution()

# 调用 isValid 方法并传递 input_str 变量作为参数
is_valid = solution.isValid("(())")

# 根据返回值 is_valid 进行处理
print(is_valid)

