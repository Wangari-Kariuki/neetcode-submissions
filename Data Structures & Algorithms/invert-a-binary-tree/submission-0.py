# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #VISIT EVery node and every time, take a look at it;s childen an  swap the spositions of the children
        #recursively run invert on left subtree and right subtree
        if not root:
            return None
        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp
        #recursively invert the subtree
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

