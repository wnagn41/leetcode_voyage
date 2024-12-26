# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        sum_length = len(list1) + len(list2)
        list_len = [0] * sum_length
        index1 = index2 =0
        new_list = []
        for s in list_len:
            if index1 >= len(list1):
                new_list.append(list2[index2])
                index2 += 1
            elif index2 >= len(list2):
                new_list.append(list1[index1])
                index1 += 1

            ##cruiial comtent
            elif list1[index1] < list2[index2]:
                new_list.append(list1[index1])
                index1 += 1
            else:
                new_list.append(list2[index2])
                index2 += 1       
        return new_list
    
    

solution = Solution()


tiem = solution.mergeTwoLists([1,2,3,4],[1,1,3,5,6,8])

# 根据返回值 is_valid 进行处理
print(tiem)
