from tree import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        assert len(nums) > 0
        it = iter(nums)
        root = cur = TreeNode(next(it))
        try:
            while cur is not None:

        except StopIteration:
            return root

sol = Solution()

if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    root = sol.sortedArrayToBST(nums)
    preorder = to_preorder(root, [])
    print(preorder)
        
