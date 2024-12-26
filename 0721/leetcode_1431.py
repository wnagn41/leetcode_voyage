class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max = candies[0]
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
        a=[]
        for i in range(len(candies)):
            if candies[i]+ extraCandies >= max:
                a.append(True)
            else:
                a.append(False)

        return a








solution = Solution()


tiem = solution.kidsWithCandies([2,3,5,1,3],3)


                 
        
print(tiem)