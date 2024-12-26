class Solution(object):
    def xorOperation(self, n, start):
        a = [start]
        b=start
        while n is not 1:
            start = start + 2
            b = b^start
            # print(start)
            a.append(start)
            n = n - 1
            

        return(b)





solution = Solution()


tiem = solution.xorOperation(5,0)


## 知识点 ： for i in range(n)    将一个行为操作n次
## 没了 ^ XOR 居然有这么强大的作用 太厉害了 每一个数字相当于判定了n个时间是对的还是错的 然后XOR 可以做什么 有什么用呢  人类为什么发明他呢 我要探索

print(tiem)