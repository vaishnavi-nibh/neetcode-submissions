# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #this is effectively the base case, where we check if we reached the bottom
        if p is None and q is None:
            return True
        
        #at this point, the check where both are None failed, so only one has to be None and the other is a node. this violates equivalency so automatically return false
        #checking if we reached the bottom of one tree but not the other
        if p is None or q is None:
            return False
        
        #if we are not at the base case (bottom) yet
        if p.val != q.val:
            return False
        
        #checking if the left and right subtrees are equivalent
        leftBool = self.isSameTree(p.left, q.left)
        rightBool = self.isSameTree(p.right, q.right)

        return leftBool and rightBool

        
        