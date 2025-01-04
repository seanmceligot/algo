from typing import Optional, List
from collections import deque
from tree import *

def breadth_first_to_list(root: Optional[TreeNode]) -> List[List[int]]:
    values: List[List[int]]= list()
    if root is not None:
        queue : Deque[Tuple[int,TreeNode]] = deque()
        queue.append((0,root)) # [root]
        count = 0
        while len(queue) > 0:
            level, cur = queue.popleft()  ## fifo retrieve starting from root and then the next added element
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
    root = build_tree_breadth_first([3,9,20,None,None,15,7])
    l = breadth_first_to_list(root)
    assert l == [[3],[9,20],[15,7]]
    drawtree(root)
