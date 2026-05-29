# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        returnList = ListNode()
        temp = returnList
        while list1 and list2:
            if list1.val <= list2.val:
                temp.val = list1.val
                list1 = list1.next
            else:
                temp.val = list2.val
                list2 = list2.next
            temp.next = ListNode()
            temp = temp.next
        
        iterVal = None
        if list1:
            iterVal = list1
        else:
            iterVal = list2
        
        while iterVal:
            temp.val = iterVal.val
            if iterVal.next != None:
                temp.next = ListNode()
            iterVal = iterVal.next
            temp = temp.next
        
        return returnList

        