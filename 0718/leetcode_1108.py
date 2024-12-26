class Solution:
    def defangIPaddr(self, address):
        stack = list(address)
        a=[]
        s=""
        for u in address:
            lip = stack.pop()
            if lip == ".":
                a.append("]" + lip + "[")
            else:
                a.append(lip)
        s = s.join(a)[::-1]
        return s







solution = Solution()


tiem = solution.defangIPaddr("255.100.50.0")

print(tiem)