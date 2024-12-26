class Solution:
    def mergeTwoLists(self, list1,list2) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2
        

solution = Solution()


tiem = solution.mergeTwoLists([1,2,3,4],[1,1,3,5,6,8])

# 根据返回值 is_valid 进行处理
print(tiem)
