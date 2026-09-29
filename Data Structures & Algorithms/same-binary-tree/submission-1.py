# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #checking the structures and the value of nodes
        if not q and not p:
            return True
        if not p or not q :
            return False
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right,q.right))
            # if rootP.left == rootQ.left:
            #     if rootP.right == rootQ.right:
            #         return True
            #     return False
        # return(self.isSameTree(p.left,q.left) and
        #     self.isSameTree(p.right,q.right))
        return False
