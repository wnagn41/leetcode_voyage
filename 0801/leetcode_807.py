class Solution(object):

    def maxIncreaseKeepingSkyline(self, grid):
        n,s,w,e = [],[],[],[]
        for i in range(len(grid)):
            max = 0
            for j in range(len(grid)):
                if grid[i][j] > max:
                    max = grid[i][j]
            w.append(max)
        for i in range(len(grid)):
            max = 0
            for j in range(len(grid)):
                if grid[j][i] > max:
                    max = grid[j][i]
            n.append(max)
            
        print(w,n)
        grid_new = []
        for i in range(len(grid)):
            grid_new.append([])
            for j in range(len(grid)):
                grid_new[i].append('0')

        for i in range(len(grid)):
            for j in range(len(grid)):
                grid_new[i][j] = [w[i],n[j]][w[i]>n[j]]
        print(grid_new)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                result += grid_new[i][j]-grid[i][j]

        return result



##知识点 如何在vscode中引入库
##知识点 如何在python中不引入库 进行任意数据的deep copy
## 知识点 [w[i],n[j]][w[i]>n[j]] 取两个数字中的较小数字 简单方法
## 知识点




solution = Solution()


tiem = solution.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]])
## reversed_list = input_list[::-1]           
        
print(tiem)