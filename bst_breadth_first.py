from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    values = list()
    if root is not None:
        queue = deque()
        queue.append((0,root))
        count = 0
        while len(queue) > 0:
            level, cur = queue.popleft()
            #print(f"level {level} cur.popleft {node.val} l:{node.left} r:{node.right}\n")
            if len(values) > level:
                values[level].append(cur.val)
            else:
                values.append([cur.val])
            print(f"values {values}\n")
            if cur.left is not None:
                queue.append((level+1, cur.left))
            if cur.right is not None:
                queue.append((level+1, cur.right))
            count += 1
    return values 


if __name__ == "__main__":
    root = TreeNode(0)
    cur = root;
    i = 0;
    for i in range(1, 22,2):
      cur.left = TreeNode(i)
      cur.right = TreeNode(i+1)
      print(cur)
      cur = cur.right;
    levelOrder(root)
