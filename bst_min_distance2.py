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
class Solution(object):
    def minDiffInBST(self, root):
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()
        print(vals)
        d = math.inf
        for i in range(len(vals) - 1):
            print(f"d = min({vals[i+1]} - {vals[i] }")
            d = min(d, vals[i+1] - vals[i] )
        return d
sol: Solution = Solution()

if __name__ == "__main__":
    #l = [4,2,6,1,3]
    l = [90,69,None,49,89,None,52]
    #l = [4,2,6,1,3]
    #l = [1,0,48,None,None,12,49]
    #l =  [3,0,48,None,None,12,49]
    root = build_tree_breadth_first(l) 
    d = sol.minDiffInBST(root)
    print(d)
    #drawtree(root)
    assert d == 1
