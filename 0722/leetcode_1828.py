class Solution(object):
    def countPoints(self, points, queries):
        ans=[]
        for i in queries:
            x = i[0]
            y = i[1]
            r = i[2]
            count = 0
            for j in points:
                x1 = j[0]
                y1 = j[1]
                dis = ((x-x1)**2+(y-y1)**2)**0.5
                if dis <= r:
                    count+=1
            ans.append(count)
        return ans

        








solution = Solution()


tiem = solution.countPoints([[1,3],[3,3],[5,3],[2,2]],[[2,3,1],[4,3,1],[1,1,2]])
        
print(tiem)