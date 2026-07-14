# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        #we use a dummy node so that we have a reference to head to return
        dummy = ListNode()
        pointer = dummy

        while list1 and list2:
            if list2.val <= list1.val:
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            
            pointer = pointer.next
        
        if list1: #if by the end of the while loop
            pointer.next = list1 #just join all of list1 (the full linkedlist) to the end of the combined list
        else: #if list2 is not null by the end of the while loop
            pointer.next = list2 #join all of list2 (the full linkedlist) to the end of the combined linkedlist
        
        return dummy.next #which points to the first non-dummy node element in the linkedlist
        