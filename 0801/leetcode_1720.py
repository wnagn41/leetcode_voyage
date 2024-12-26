class Solution(object):
    def sdecode(self, encoded, first):
        n=len(encoded)
        arr=[0]*(n+1)
        arr[0]=first
        for i in range(1,n+1):
            arr[i]=encoded[i-1]^arr[i-1]
        return arr



solution = Solution()

## 知识点： XOR如何巡行两个数字
## 知识点： 如何逆向运行 XOR
## 知识点： 交换x y的值
# x = x ^ y // (a ^ b, b)
# y = x ^ y // (a ^ b, a ^ b ^ b) => (a ^ b, a)
# x = x ^ y // (a ^ b ^ a, a) => (b, a)

tiem = solution.sdecode([1,2,3],1)

              
print(tiem)