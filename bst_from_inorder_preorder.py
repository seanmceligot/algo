from typing import Optional, List
'''
  Construct Binary Tree from Inorder and Postorder Traversal
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode({self.val})"
 
def build_node(label: str, inorder: List[int], in_start:int, in_end: int,preorder: List[int], pre_start:int, pre_end:int) -> Optional[TreeNode]:
    '''
        build tree node from inorder and postorder
    '''
    print(f"{label} inorder {inorder[in_start:in_end]}")
    print(f"{label} preorder {preorder[pre_start:pre_end]}")
    assert in_start<=in_end
    assert pre_start<=pre_end
    if in_start == in_end or pre_start == pre_end:
        print(f"leaf")
        return None
    root_val = preorder[pre_start]
    print(f"root_val {root_val}")
    root = TreeNode(root_val)
    
    index_of_root_val_in_inorder = inorder.index(root_val)
    assert index_of_root_val_in_inorder >=0
    # ex, I=3, lef_size=3
    #l inorder  [l,l,l,I,r,r,r]
    #  preorder [I,l,l,l,r,r,r]
    left_size = index_of_root_val_in_inorder-in_start
    left_in_start = in_start
    left_in_end = in_start+left_size #exclusive
    right_in_start = in_start+left_size+1 #inclusive
    right_in_end = in_end
    
    left_pre_start = pre_start+1
    left_pre_end = pre_start+left_size+1 #exclusive
    right_pre_start = pre_start+left_size+1 #inclusive
    right_pre_end = pre_end

    left_in_len =  left_in_end - left_in_start;
    left_pre_len =  left_pre_end - left_pre_start;
    right_in_len =  right_in_end - right_in_start;
    right_pre_len =  right_pre_end - right_pre_start;
    print(f"left_in_len {left_in_len}")
    print(f"left_pre_len {left_pre_len}")
    print(f"right_in_len {right_in_len}")
    print(f"right_pre_len {right_pre_len}")
    assert left_in_len  ==  left_pre_len
    assert right_in_len  ==  right_pre_len
    assert left_in_len < in_end-in_start
    root.left = build_node("left", inorder, left_in_start, left_in_end, preorder, left_pre_start, left_pre_end)
    root.right =build_node("right", inorder, right_in_start, right_in_end, preorder, right_pre_start, right_pre_end)
    return root


def build_tree(inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
    n:int = len(inorder)
    if n == 0: 
        return None;
    return build_node("start", inorder, 0, n, preorder, 0, n)

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
    
def main():
    inorder  = [ 4, 2, 1, 7, 5, 8, 3, 6 ]
    preorder = [ 1, 2, 4, 3, 5, 7, 8, 6 ]
    root = build_tree(inorder, preorder)
    
    preorder = to_preorder(root, [])

    inorder2 = to_inorder(root, [])
    print(f"inorder {inorder}")
    print(f"inorder2 {inorder2}")
    assert inorder2 == inorder

    preorder2 = to_preorder(root, [])
    print(f"preorder {preorder}")
    print(f"preorder2 {preorder2}")
    assert preorder2 == preorder

if __name__ == '__main__':
    main()
