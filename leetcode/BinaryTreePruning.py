# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def f(self, root):
        if root is None:
            return None

        root.left = self.f(root.left)
        root.right = self.f(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None
            
        return root    
                

    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root = self.f(root)

        return root
        
