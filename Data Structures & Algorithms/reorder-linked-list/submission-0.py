# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        '''note: at the end of the while loop, slow points to the last element in the first half
        ex: [0,1,2,3,4,5,6] at the end of the while loop, slow = 3 and fast = 6
        therefore, the start of the second half that we can reverse to easily apply the n-1, n-2 retrieval
        starts 1 after slow'''

        current = slow.next 
        slow.next = None #disconnect the first half of the linkedlist from the second half
        '''this avoids any mistakes when we merge the two linkedlists together again
        even tho we may successfully reverse the second half, if we dont disconnect the lists from each other initially
        we may form cycles or links that we no longer care for'''

        prev = None
        while current:
            next_elem = current.next
            current.next = prev
            prev = current
            current = next_elem

        second_half = prev
        first_half = head

        while second_half:
            first_next = first_half.next
            second_next = second_half.next

            first_half.next = second_half
            second_half.next = first_next

            first_half = first_next
            second_half = second_next
