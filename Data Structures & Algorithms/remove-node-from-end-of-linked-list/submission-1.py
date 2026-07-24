# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #reverse the list
        current = head
        prev = None
        
        #Reversing the linkedlist
        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem

        #new head is the start of the reversed linkedlist
        new_head = prev
        current = new_head
        #This is to identify the element to remove
        prev_Node = None
        position_from_back = 1

        while position_from_back < n:
            prev_Node = current
            current = current.next #going towards the node we have to remove
            position_from_back += 1
        
        #if there is only 1 element in the linkedlist or the element we are attempting to delete is head
        if prev_Node is None:
            new_head = current.next #we just need to remove the connection between current and the next
            '''we dont access prev_Node if the node we are trying to remove is the last in the original list
            (n=1) because prev_Node is none'''
        else: 
            prev_Node.next = current.next

        #now reverse the linkedlist back:
        current = new_head
        prev = None

        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        
        head = prev
        return head
        



