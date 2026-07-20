def invertTree(root):
  if not root:
    return None
    root.left, root.right = root.right, root.left
    self.invertTree(root.Left)
    self.invertTree(root.right)
    return root
