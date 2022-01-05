from tree import *
import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# distance = 
# root.val - left.val
# mindist(1, 0) -> 1
# mindist(49, 48) -> 1
# mindist()
def dfs_collect(node: Optional[TreeNode], vals) -> None:
  if not node:
    return
  vals.append(node.val)
  dfs_collect(node.left, vals)
  dfs_collect(node.right, vals)

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals = []
        dfs_collect(root, vals) ##1
        d = math.inf
        ordered = sorted(vals)
        last = ordered[0]
        print(ordered)
        for val in ordered[1:]:
            d = min(d, val-last)
            print(val, last, d)
            last = val
        if d == math.inf:
          return 0
        return int(d)
sol: Solution = Solution()

if __name__ == "__main__":
    #l = [4,2,6,1,3]
    l = [90,69,None,49,89,None,52]
    l = [4,2,6,1,3]
    l = [1,0,48,None,None,12,49]
    #l =  [3,0,48,None,None,12,49]
    root = build_tree_breadth_first(l) 
    d = sol.minDiffInBST(root)
    print(d)
    #drawtree(root)
    assert d == 1
