# Python3 Solution
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.total_sum += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)

        self.total_sum = 0
        dfs(root)
        return self.total_sum
