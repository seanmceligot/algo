
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build(node: Optional[TreeNode], inorder: List[int], int index) -> Optional[TreeNode]:
    left=right=parent=None
    if index < len(inorder):
        left = TreeNode(inorder[index]);
        index+=1
    else:
        return node
    if index < len(inorder):
        parent = TreeNode(inorder[index]);
        index+=1
    if index < len(inorder):
        right = TreeNode(inorder[index]);
        index+=1
    if parent is not None:
        parent.left = left
        parent.right = right
    if node is None:
        node = TreeNode
    n
        
    
    if node:
    else:
        
    
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        build(None, inorder, 0 )    
