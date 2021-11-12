from typing import Optional, List
from collections import deque
from tree import TreeNode


def lr_sym(left: Optional[TreeNode], right: Optional[TreeNode] ):
    if left is None:
        return right is None
    if right is None:
        return False
    return left.val == right.val and lr_sym(left.left,  right.right) and lr_sym(left.right, right.left)

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True;
        left = root.left
        right = root.right;
        return lr_sym(left, right)

if __name__ == "__main__":
    root = TreeNode(0)
    cur = root;
    i = 0;
    #for i in range(1, 22,2):
    cur.left = TreeNode(i)
    cur.right = TreeNode(i)
    print(cur)
    #cur = cur.right;
    s = Solution()
    is_sym = s.isSymmetric(root)
    print(is_sym)
