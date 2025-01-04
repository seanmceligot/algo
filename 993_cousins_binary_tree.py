# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# (starting point) Given the root of
# PREREQ: a binary tree
# PREREQ: with unique values
# INPUT: and the values of two different nodes of the tree x and y,

# RETURN: return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.

# Two nodes of a binary tree are cousins
# if they have the same (TEST 1) depth
# with different parents (TEST 2).

# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
from collections import deque
from tree import TreeNode, build_tree_breadth_first, print_tree, print_tree2
from typing import Optional, Deque, Tuple

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root is None:
            return False
        xy = [x,y]
        print(xy)
        if root.left and root.left.val in xy:
            return False
        if root.right and root.right.val in xy:
            return False

        q: Deque[Tuple[TreeNode, Optional[TreeNode]]] = deque([(root, None)])
        depth = 0
        xdepth = ydepth = None
        xparent: Optional[TreeNode] = None
        yparent: Optional[TreeNode] = None
        while q:
            size = len(q)
            for _ in range(size):
                (node, parent) = q.popleft()
                print(f"node {node.val} depth {depth} parent {parent} size {size} q {q}")
                # the are childen so not cousins
                if node.val == y:
                    ydepth = depth
                    yparent = parent
                if node.val == x:
                    xdepth = depth
                    xparent = parent
                if node.left:
                    q.append( (node.left, node))
                if node.right:
                    q.append( (node.right, node))
                print(f"node {node.val} depth {depth}  parent {parent} xdepth {xdepth} ydepth {ydepth}")
                if xdepth and ydepth:
                    # with different parents (TEST 2).
                    if xparent == yparent:
                        return False
                    # if they have the same (TEST 1) depth
                    return xdepth == ydepth
            depth+=1
        return False

if __name__ == "__main__":
    root = build_tree_breadth_first( [1,2,3,None,4,None,5] )
    #     1
    #   2   3
    #  x 4   x 5
    if not root:
        raise Exception("build_tree_breadth_first failed")

    print_tree(root)
    print("")
    #import pdb; pdb.set_trace()
    print(Solution().isCousins(root, 4, 5))
    print_tree2(root)
