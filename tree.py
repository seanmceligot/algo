
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def build_tree(count):
    root = TreeNode(0)
    for i in range(1, count):
      cur.left = TreeNode(i)
      cur.right = TreeNode(i+1)
      cur = cur.right
    return root
