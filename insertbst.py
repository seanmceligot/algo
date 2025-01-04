def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    newnode = TreeNode(val)
    if root is None:
        root = newnode
        return root

    cur = root
    while cur:
        if cur.val == val:
            return root
        if newnode.val < cur.val:
            if cur.left is None:
                cur.left = newnode
                return root
            else:
                cur = cur.left
        if newnode.val > cur.val:
            if cur.right is None:
                cur.right = newnode
                return root
            else:
                cur = cur.right
