class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        stack = list(command)
        a=[]
        b=[]
        for i in command:
            s_pop = stack.pop()
            if s_pop == 'G':
                a.append('G')
            if s_pop == ')':
                b.append(')')
            if s_pop == 'a':
                a.append('a')
            if s_pop == 'l':
                b.pop()
                a.append('l')
            if s_pop == '(':
                if b:
                    a.append('o')
                    b.pop()

        
            
        print (a)
        reversed_string = ''.join(a[::-1])
        return(reversed_string)


solution = Solution()


tiem = solution.interpret("(al)G(al)()()G")

# 根据返回值 is_valid 进行处理
print(tiem)