# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        #we need somethingthat points to the head of the combined linkedlist
        head = None
        #we then need something to keep track of our current position in the combined linkedlist
        current = None

        if not list1 and not list2:
            return None
        elif list1 and not list2:
            return list1
        elif list2 and not list1:
            return list2

        if list1.val < list2.val:
            head = list1
            current = head
            list1 = list1.next 
        else:
            head = list2
            current = head
            list2 = list2.next
        
        
        while list1 and list2: #the while loop should go while both lists are not null
            if list1.val < list2.val:
                current.next = list1 #add list1 to the list
                current = list1
                list1 = list1.next #move to the next comparison
            else:
                current.next = list2
                current = list2
                list2 = list2.next
    
        if list1: #if list1 is not null (but list2 was which is why we left the loop)
            current.next = list1
        elif list2:
            current.next = list2
        
        return head

        