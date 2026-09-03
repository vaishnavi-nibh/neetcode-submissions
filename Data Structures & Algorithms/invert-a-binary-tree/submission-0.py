# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        stack = [root]
        
        #while there are still unvisited nodes
        while stack:
            current = stack.pop()
            
            leftnode = current.left
            rightnode = current.right
            current.left = rightnode
            current.right = leftnode

            if leftnode != None:
                stack.append(leftnode)
            if rightnode != None:
                stack.append(rightnode)
            
        return root



