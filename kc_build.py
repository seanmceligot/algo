from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode({self.val})"

def build_tree_node(inorder: List[int], in_start:int, in_end:int, postorder: List[int], post_start:int, post_end:int) -> Optional[TreeNode]:
        assert in_end>= in_start
        assert post_end >= post_start

        if in_start == in_end or post_start == post_end: 
            return None
        root_val:int = postorder[post_end-1]
        root = TreeNode(root_val);
        index_of_root_in_inorder:int = -1;
        for i in range(in_start, in_end):
            if root_val == inorder[i]:
                index_of_root_in_inorder = i;
                break;
        assert index_of_root_in_inorder >= 0
        left_size: int            = index_of_root_in_inorder - in_start

        left_in_start:int = in_start
        left_in_end: int = in_start + left_size
        right_in_start: int = left_in_end+1
        right_in_end: int = in_end

        left_post_start:int = post_start
        left_post_end: int  = post_start+left_size
        right_post_start     = left_post_end
        right_post_end: int  = post_end-1 # this was the root

        root.left =  build_tree_node(inorder, left_in_start, left_in_end,  postorder, left_post_start, left_post_end )
        root.right = build_tree_node(inorder, right_in_start, right_in_end, postorder, right_post_start, right_post_end)
        return root

def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    n:int = len(inorder)
    if n == 0: 
        return None;
    return build_tree_node(inorder, 0, n, postorder, 0, n)


def to_preorder(node, l:List[int]) -> List[int]:
    if node == None:
        return l
    l.append(node.val)
    l = to_preorder(node.left, l)
    l = to_preorder(node.right, l)
    return l
def to_inorder(node, l:List[int]) -> List[int]:
    if node == None:
        return l
    l = to_inorder(node.left, l)
    l.append(node.val)
    l = to_inorder(node.right, l)
    return l
def to_postorder(node, l:List[int]) -> List[int]:
    if node == None:
        return l
    l = to_postorder(node.left, l)
    l = to_postorder(node.right, l)
    l.append(node.val)
    return l

if __name__ == '__main__':
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    postorder = [8, 4, 5, 2, 6, 7, 3, 1]
    root = build_tree(inorder, postorder)
    preorder = to_preorder(root, [])
    print(preorder)
    assert preorder == [1, 2, 4, 8, 5, 3, 6, 7]

    inorder2 = to_inorder(root, [])
    print(inorder)
    assert inorder2 == inorder

    postorder2 = to_postorder(root, [])
    print(postorder)
    assert postorder2 == postorder
