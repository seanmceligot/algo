from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode({self.val})"
def buildTree( inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder:
        return None
    elif len(inorder) == 1:
        return TreeNode(inorder[0])
    else:
        root = TreeNode(postorder[-1])
        idx = inorder.index(root.val)
        root.left = buildTree(inorder[:idx], postorder[:idx])
        root.right = buildTree(inorder[idx+1:], postorder[idx:])
        return root
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
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = buildTree(inorder, postorder)

    preorder = to_preorder(root, [])
    print(preorder)

    inorder2 = to_inorder(root, [])
    print(f"inorder {inorder}")
    print(f"inorder2 {inorder2}")
    assert inorder2 == inorder

    postorder2 = to_postorder(root, [])
    print(f"postorder {postorder}")
    print(f"postorder2 {postorder2}")
    assert postorder2 == postorder
