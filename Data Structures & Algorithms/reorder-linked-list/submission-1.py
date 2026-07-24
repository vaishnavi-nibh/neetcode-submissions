# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #by the time fast gets to the end of the linkedlist, slow is at the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

        second_half = slow.next
        slow.next = None #disconnecting the first half 

        current = second_half
        prev = None

        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem
        
        #at this point, the second half of the linkedlist has been reversed
        first_half = head
        curr_Node = prev

        while curr_Node:
            next_elem_first = first_half.next
            first_half.next = curr_Node
            next_elem_second = curr_Node.next
            curr_Node.next = next_elem_first
            curr_Node = next_elem_second
            first_half = next_elem_first
        

