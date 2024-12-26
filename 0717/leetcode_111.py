class Solution:
    def minDepth(self, root):
        def dfs(root, level):
            if  not root.left and  not root.right:
                return level
            ans=2**31
            if root.left:
                ans=min(ans, dfs(root.left, level+1))
            if root.right:
                ans=min(ans, dfs(root.right, level+1))
            return ans
        
        if not root: 
            return 0
        return dfs(root, 1)
    



//我他妈实在是不会写了 这些python内部的数据结构 但是我不知道怎么直接调用的 比如listnode和binarytree到底还有多少啊//
//求求你别再折磨我了//
// 看起来这段代码的意思貌似是递归地查找这个数列的每一个左子树和每一个右子树
//但是他好像但是这里的二叉树好像不是一个完全二叉树，
好像他只要求上层的数比下层的数小除此之外什么都没有要求，
所以说他的方式好像就是每深化一层就把层数加一同时递归地去寻找下一层直到左子树和右子树都为空为止，
然后再查找这种情况下能得到的最大的深度仅此而已//
solution = Solution()


tiem = solution.minDepth([3,9,20,null,null,15,7])

# 根据返回值 is_valid 进行处理
print(tiem)