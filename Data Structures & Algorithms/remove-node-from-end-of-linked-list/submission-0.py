# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #step 1: reverse the linked list
        prev = None
        current = head

        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        
        #so now, prev points to the start of the reversed linkedlist
        head_new = prev
        current = head_new
        #we also want to maintain previous pointer so lets do:
        previous = None
        #now the linkedlist is reversed
        while n > 1:
            n -= 1
            previous = current
            current = current.next
        
        #we are now at the node that we want to remove
        #and we are keeping track of the previous node using the prev pointer
        #handle edge case where n = 1(we are removing the head), in this case previous is None
        if previous is None:
            head_new = current.next #the head of the new list is now pointing to the next element in the linkedlist
        else:
            previous.next = current.next
    
        #now we want to once again reverse this linkedlist, so we'll start with head_new
        #again lets do prev = None
        prev = None
        current = head_new
        
        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        
        #now once again we return prev
        return prev

        

            
