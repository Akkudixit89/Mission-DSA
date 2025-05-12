class Solution:
  def lowestCommonAncestor(
      self,
      root: TreeNode | None,
      p: TreeNode | None,
      q: TreeNode | None,
  ) -> TreeNode | None:
    q_ = collections.deque([root])
    parent = {root: None}
    ancestors = set()  
    while p not in parent or q not in parent:
      root = q_.popleft()
      if root.left:
        parent[root.left] = root
        q_.append(root.left)
      if root.right:
        parent[root.right] = root
        q_.append(root.right)

    while p:
      ancestors.add(p)
      p = parent[p]  
    while q not in ancestors:
      q = parent[q]

    return q
