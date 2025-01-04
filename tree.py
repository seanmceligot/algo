from typing import Optional, Any, List, Self, Deque, Tuple
import turtle
from os import popen
from collections import deque
from icecream import ic


class TreeNode:
    def __init__(
        self, val: int, left: Optional[Self] = None, right: Optional[Self] = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def new_node(
    val: Any, left: Optional[TreeNode] = None, right: Optional[TreeNode] = None
) -> TreeNode:
    return TreeNode(val, left, right)


# def val(n: Optional[TreeNode]) -> str:
#    return n.val if n is not None else "None"


def eq(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return False
    return a.val == b.val


def lte(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return False
    return a.val <= b.val


def lt(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return False
    return a.val < b.val


def gte(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return False
    return a.val >= b.val


def gt(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    if a is None or b is None:
        return False
    return a.val > b.val


def preOrder(node: Optional[TreeNode]):
    if node:
        print(node.val, end=" ")
        if node.left:
            preOrder(node.left)
        if node.right:
            preOrder(node.right)


def to_preorder(node, l: List[int] = []) -> List[int]:
    if node == None:
        return l
    l.append(node.val)
    l = to_preorder(node.left, l)
    l = to_preorder(node.right, l)
    return l


def to_inorder(node, l: List[int] = []) -> List[int]:
    if node == None:
        return l
    l = to_inorder(node.left, l)
    l.append(node.val)
    l = to_inorder(node.right, l)
    return l


def to_postorder(node, l: List[int] = []) -> List[int]:
    if node == None:
        return l
    l = to_postorder(node.left, l)
    l = to_postorder(node.right, l)
    l.append(node.val)
    return l


"""
build_tree_breadth_first

LeetCode uses a level-order traversal (breadth-first search) representation for trees in array format. Here's how it works:

How the Array Format Represents a Tree
Root Node:

The first element of the array is the root node.
Left and Right Children:

For a node at index i:
The left child is at index 2 * i + 1.
The right child is at index 2 * i + 2.
null for Missing Nodes:

null represents a missing node (e.g., no child at that position).
Traversal Order:

The array is filled level by level, from left to right.
"""


def build_tree_breadth_first(ar: List[Optional[int]]) -> Optional[TreeNode]:
    if len(ar) < 1:
        return None
    # convert list of int to list of nodes
    nodes = [None if val == None else TreeNode(val) for val in ar]
    ic(nodes)
    kids = nodes[::-1]
    ic(kids)
    root = kids.pop()  # remove the last kids (first in ar)
    for node in nodes:
        ic(node)
        if node:
            if kids:
                node.left = kids.pop()
                ic(node.left, kids)
            if kids:
                node.right = kids.pop()
                ic(node.right, kids)
    return root


def build_tree_breadth_first2(ar: List[Optional[int]]) -> Optional[TreeNode]:
    if not ar:
        return None

    # Convert list of values to TreeNode instances (or None for null nodes)
    nodes = [None if val is None else TreeNode(val) for val in ar]

    # Initialize a queue and add the root node
    queue = deque()
    root = nodes[0]
    queue.append(root)

    # Start processing the queue to build the tree
    i = 1  # Pointer to track the position in the nodes list
    while queue and i < len(nodes):
        current = queue.popleft()  # Get the current node from the queue
        if current:  # If the current node is not None
            # Assign the left child, if available
            ic(current, i, nodes)
            if i < len(nodes):
                current.left = nodes[i]
                queue.append(nodes[i])  # Add left child to the queue
                i += 1
            # Assign the right child, if available
            if i < len(nodes):
                current.right = nodes[i]
                queue.append(nodes[i])  # Add right child to the queue
                i += 1
    return root


def get_console_width() -> int:
    out = popen("stty size").read()
    print(out)
    _, cols = out.split()
    return int(cols)


def breadth_first_to_list(root: Optional[TreeNode]):
    if root is not None:
        queue: Deque[Tuple[int, TreeNode]] = deque()
        yield root
        queue.append((0, root))
        count = 0
        while len(queue) > 0:
            level, cur = queue.popleft()
            # print(f"level {level} cur.popleft {node.val} l:{node.left} r:{node.right}\n")
            if cur.left is not None:
                queue.append((level + 1, cur.left))
            if cur.right is not None:
                queue.append((level + 1, cur.right))
            count += 1


def drawtree(root: Optional[TreeNode]):
    if not root:
        return

    def height(root: Optional[TreeNode]) -> int:
        return 1 + max(height(root.left), height(root.right)) if root else 0

    def jumpto(x: int, y: int):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw_one_node(node: Optional[TreeNode], x: int, y: int, dx: int):
        if node is not None:
            t.goto(x, y)
            jumpto(x, y - 20)
            t.write(node.val, align="center", font=("Arial", 22, "normal"))
            if node.left:
                draw_one_node(node.left, x - dx, y - 60, round(dx / 2))
            jumpto(x, y - 20)
            if node.right:
                draw_one_node(node.right, x + dx, y - 60, round(dx / 2))

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw_one_node(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.exitonclick()
    try:
        turtle.mainloop()
    except:
        pass


def print_tree2(root: Optional[TreeNode]):
    if not root:
        print("Empty Tree")
        return

    levels: List[List[int]] = []
    queue: Deque[Tuple[TreeNode, int]] = deque()
    queue.append((root, 0))
    while queue:
        node, level = queue.popleft()
        if len(levels) <= level:
            levels.append([])
        if node:
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        # else:
        #    levels[level].append(None)

    for i, level in enumerate(levels):
        print("Level", i, ":", level)


def print_tree(root: Optional[TreeNode]):
    # depth 1 : center screen_with/2
    # dpeth 2 : center screen_with/4 spaces
    if root is None:
        return
    queue: Deque[Tuple[int, TreeNode]] = deque()
    screen_width = 40  # get_console_width() - 20
    queue.append((1, root))
    last_depth = 1
    while len(queue) > 0:
        depth, cur = queue.popleft()
        if depth != last_depth:
            print("")
            last_depth = depth
        strval: str = str(cur.val) if cur.val != -1 else "__"
        spaces: int = int(screen_width / (depth + 1))
        print(f"{strval.rjust(spaces, ' ')}", end="")
        if cur.left or cur.right:
            # print empties for spacing
            queue.append(
                (depth + 1, cur.left if cur.left is not None else TreeNode(-1))
            )
            queue.append(
                (depth + 1, cur.right if cur.right is not None else TreeNode(-1))
            )


if __name__ == "__main__":
    # drawtree(build_tree_breadth_first([1,2,3,null,null,4,null,null,5]))
    # drawtree(build_tree_breadth_first([2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]))
    # jroot = build_tree_breadth_first( [3,5,1,6,2,0,8,-1,-1,7,4])
    root = build_tree_breadth_first2([1, 2, 3, None, 4, None, 5])
    ic(root)

    # drawtree(root)
    print_tree(root)
