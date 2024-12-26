class Solution(object):
    def rotate(self, matrix):
        length_matrix = len(matrix)
        print (length_matrix)
        new_matrix = []
        for i in range(length_matrix):
            new_matrix.append([])
            for j in range(length_matrix):
                new_matrix[i].append(0)
        for i in range(length_matrix):
            for j in range(length_matrix):
                new_matrix[j][i] = matrix[i][j]
        print(new_matrix)
        for i in range(length_matrix):
            for j in range(length_matrix):
                matrix[i][length_matrix-j-1] = new_matrix[i][j]
        return matrix
            
        


solution = Solution()

## 知识点：有没有一种条件能在判断条件后 进入两种不同的case

## 本来我想考从外环向里环 一层层旋转 但是现在我发现这很困难 因为不知道怎么写旋转
## 顺时针旋转 就是沿着00 - nn 轴翻转 然后横向翻转

## 一个从0:5
# 0:4 1:3 2:3
# 一个从0:7
# 0:6 1:5 2:4

##  create a matrix as large as matrix
        # for i in range(length_matrix):
        #     new_matrix.append([])
        #     for j in range(length_matrix):
        #         new_matrix[i].append(0)
tiem = solution.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])

              
print(tiem)