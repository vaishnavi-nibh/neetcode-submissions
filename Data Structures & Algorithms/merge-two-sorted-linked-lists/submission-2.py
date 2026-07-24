# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        head = None

        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2

        if list1.val < list2.val:
            head = list1
            current = head
            #now increment list1 so that we prepare to check the next node in the linkedlist
            list1 = list1.next
        else:
            head = list2
            current = head
            #incrementing list2 so that we prepare to check the next node in the linkedlist
            list2 = list2.next
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                current = list1
                list1 = list1.next
            else:
                current.next = list2
                current = list2
                list2 = list2.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return head