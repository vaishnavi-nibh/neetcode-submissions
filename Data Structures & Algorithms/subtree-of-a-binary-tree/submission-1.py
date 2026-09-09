# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #first we check, if we have gotten to the bottom and they both are None, return true
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
 
        if p.val != q.val:
            return False
        
        leftTree = self.isSameTree(p.left, q.left)
        rightTree = self.isSameTree(p.right, q.right)

        return leftTree and rightTree


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #if we've reached the bottom and haven't found the subtree
        if root is None:
            return False
        
        #at each root, check if isSameTree starting from this point, is the same
        if self.isSameTree(root, subRoot):
            return True
        
        leftSubtree = self.isSubtree(root.left, subRoot)
        rightSubtree = self.isSubtree(root.right, subRoot) 

        return leftSubtree or rightSubtree
    
        

