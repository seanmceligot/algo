from typing import Optional, List
from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    def __repr__(self):
        return f"Node({self.val})"

def levelOrder(root: Node) -> Node
    if root is None or root.left is None or root.right is None:
        return root
    root.left.next = root.right
    if root.next is not None:
        root.right.next = root.next.left
    self.connect(root.left)
    self.connect(root.right)
    return root
        

def to_inorder(node, l:List[int]) -> List[int]:
    if node == None:
        return l
    l = to_inorder(node.left, l)
    l.append(node.val)
    l = to_inorder(node.right, l)
    return l

if __name__ == "__main__":
    root = Node(0)
    cur = root;
    i = 0;
    for i in range(1, 7,2):
      cur.left = Node(i)
      cur.right = Node(i+1)
      print(cur)
      cur = cur.right;
    levelOrder(root)
