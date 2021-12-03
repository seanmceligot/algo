import math
from typing import Optional
from tree import *
def is_valid(root: Optional[TreeNode], lowest: int, highest:int) -> bool:
    if not root:
        return True
    val = root.val
    if val <= lowest:
      return False
    if val >= highest:
      return False  
    # left and right
    #   true if left and right are true
    # left only
    #   true if left is true
    # right only 
    #   true if right is true
    # right is None and left is None
    #   true 
    if root.left:
      if root.left.val >= val:
        #print(f"{root.left.val} > {val}")
        return False
      if not is_valid(root.left, lowest, val):
        return False
    if root.right:
      if root.right.val <= val:
        #print(f"{root.right.val} < {val}")
        return False
      return is_valid(root.right, val, highest)
    return True
if __name__ == '__main__':
    root = build_tree_breadth_first([5,4,6,None,None,3,7])
    #drawtree(root)
    if root:
        llim = int(math.pow(-2, 31))
        ulim = int(math.pow(2, 31))
        print(is_valid(root, llim, ulim))
