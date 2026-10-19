# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #we need to carry the maximum value seen so  far on the current path
        #if the current nodes value is greater than the previous node value
        def dfs (node, maxValue):
            if not node:
                return 0
            if node.val >= maxValue:
                count =  1
            else:
               count = 0
            maxValue = max(maxValue, node.val)
            count += dfs(node.left, maxValue)
            count += dfs(node.right, maxValue)
            return count
        return dfs(root, root.val)