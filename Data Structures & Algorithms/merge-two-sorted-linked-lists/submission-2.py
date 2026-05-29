# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        newList = ListNode()
        temp = newList
        while list1 and list2:
            if list1.val <= list2.val:
                temp.val = list1.val
                temp.next = ListNode()
                temp = temp.next
                list1 = list1.next
            else:
                temp.val = list2.val
                temp.next = ListNode()
                temp = temp.next
                list2 = list2.next
        if list1:
            longList = list1
        else:
            longList = list2

        while longList:
            temp.val = longList.val
            if longList.next:
                temp.next = ListNode()
            temp = temp.next
            longList = longList.next
        
        
        return newList

        