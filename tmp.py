
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def is_leaf(node: TreeNode) -> bool:
    return node.left is None and node.right is None

def root_to_leaf_find_sum(node: Optional[TreeNode], path: deque, sum: int, targetSum: int) -> bool:
    #print(f"root_to_leaf_find_sum {node} {sum} {path}\n")
    if node is None:
        return False
    val = node.val if node.val is not None else 0
    sum += val
    path.append(node);
    if is_leaf(node) and sum == targetSum:
        #print(f"found {targetSum} ∑ {sum} {path}\n")
        return True
    #print(f"not found {targetSum} ∑ {sum} {path}\n")
    if node.left:
        #print(f"calling left {node.left} ∑ {sum} {path}\n")
        if root_to_leaf_find_sum(node.left, path, sum, targetSum):
            return True
    if node.right:
        #print(f"calling right {node.left} ∑ {sum} {path}\n")
        if root_to_leaf_find_sum(node.right, path, sum, targetSum):
            return True
    path.pop()
    return False

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    path: deque = deque()
    return root_to_leaf_find_sum(root, path, 0, targetSum)
    
if __name__ == "__main__":
    input = [-2,None,-3]
    i = 1;
    root = cur= TreeNode(input[0])
    while i < len(input):
        cur.left = TreeNode(input[i])
        i+=1
        cur.right = TreeNode(input[i])
        i+=1
    #print(root.val, root.left.val, root.right.val)
    hasPathSum(root, -5)
   
def fill_range():
    for i in range(1, 8,2):
      cur.left = TreeNode(i+2)
      cur.right = TreeNode(i+3)
      #print(cur)
      cur = cur.right;
