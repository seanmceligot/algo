from typing import Optional, List
from tree import *


def build_node(
    inorder: List[int],
    in_start: int,
    in_end: int,
    postorder: List[int],
    post_start: int,
    post_end: int,
) -> Optional[TreeNode]:
    assert in_start <= in_end
    assert post_start <= in_end
    if in_start == in_end or post_start == post_end:
        return None
    root_val = postorder[post_end - 1]
    root = TreeNode(root_val)

    index_of_root_val_in_inorder = inorder.index(root_val)
    assert index_of_root_val_in_inorder >= 0
    left_size = index_of_root_val_in_inorder - in_start
    left_in_start = in_start
    left_in_end = in_start + left_size
    right_in_start = left_in_end + 1
    right_in_end = in_end

    left_post_start = post_start
    left_post_end = post_start + left_size
    right_post_start = left_post_end
    right_post_end = post_end - 1
    root.left = build_node(
        inorder, left_in_start, left_in_end, postorder, left_post_start, left_post_end
    )
    root.right = build_node(
        inorder,
        right_in_start,
        right_in_end,
        postorder,
        right_post_start,
        right_post_end,
    )
    return root


def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    n: int = len(inorder)
    if n == 0:
        return None
    return build_node(inorder, 0, n, postorder, 0, n)


if __name__ == "__main__":
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    root = build_tree(inorder, postorder)

    preorder = to_preorder(root, [])

    inorder2 = to_inorder(root, [])
    print(f"inorder {inorder}")
    print(f"inorder2 {inorder2}")
    assert inorder2 == inorder

    postorder2 = to_postorder(root)
    print(f"postorder {postorder}")
    print(f"postorder2 {postorder2}")
    assert postorder2 == postorder
