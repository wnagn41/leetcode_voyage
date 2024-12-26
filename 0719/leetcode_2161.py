class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        st = nums[::-1]
        pivot_num = [pivot]
        a = []
        b = []
        c = []
        for i in nums:
            if i < pivot:
                a.append(i)
            if i > pivot:
                b.append(i)
            if i == pivot:
                c.append(i)

        list1_str = [num for num in a]
        list2_str = [num for num in b]
        list3_str = [num for num in c]

        # Join the strings in both lists to create a new string
        new_string = list1_str + list3_str + list2_str
        return(new_string)


        ## Is there such a data structure or class. it is more effective then list and number can be added on both side
solution = Solution()


tiem = solution.pivotArray([9,12,5,10,14,3,10],10)

print(tiem)