from tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
  
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      if q is None and q is None: # both none
        return True
      if p is None or q is None: # only one is none
         return False
      if p.val != q.val:
        return False
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
