# lowest common ancestor
from tree import *


def is_in_subtree(root: Optional[TreeNode], val):
    if root is None:
        return False
    if root.val == val:
        print(f"found {val}")
        import pdb

        pdb.set_trace()
        return True
    return is_in_subtree(root.left, val) or is_in_subtree(root.right, val)


def loop(desc: str, root: "Optional[TreeNode]", p: "TreeNode", q: "TreeNode"):
    if root is None:
        return None
    #     5
    # 1       9
    # if l is 6+ go right
    # if r 5- go left
    print(f"-{desc}   {val(root)}                     p {val(p)} q {val(q)}")
    print(f"-{desc} {val(root.left)}    {val(root.right)}")

    if gte(root.left, root):
        return loop("gte", root.left, p, q)
    if lte(root.right, root):
        return loop("lte", root.left, p, q)
    if eq(root, p):
        print(f"root is p {val(p)}")
        if is_in_subtree(root.right, q):
            print(
                f"root,p,right {desc} r {val(root)} l {val(root.left)} r {val(root.right)} p {val(p)} q {val(q)}"
            )
            return root
        if is_in_subtree(root.left, q):
            print(
                f"root,p,peft {desc} r {val(root)} l {val(root.left)} r {val(root.right)} p {val(p)} q {val(q)}"
            )
            return root
    is_left = eq(root, p) or is_in_subtree(root.left, p)
    is_right = eq(root, p) or is_in_subtree(root.right, p)

    if is_left and is_right:
        return root
    # not left and right, so try
    # left = loop("left", root.left, l, r)
    # if left is not None:
    #    return left
    # right = loop("right", root.right, l, r)
    # if right is not None:
    #    return right;
    return None


if __name__ == "__main__":
    root = build_tree_breadth_first([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    p = TreeNode(5)
    q = TreeNode(4)
    lca = loop("start", root, p, q)
    print(lca)
