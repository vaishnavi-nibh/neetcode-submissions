# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head #slow should increment by 1
        fast = head #fast should increment by 2

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True #it is a cycle, they eventually caught up
        
        return False
