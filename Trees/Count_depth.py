class Solution:
  def count_depth(self, root):
    if not root:
      return 0
    left = self.count_depth(root.left)
    right = self.count_depth(root.right)
    return 1 + max(left,right)
      
