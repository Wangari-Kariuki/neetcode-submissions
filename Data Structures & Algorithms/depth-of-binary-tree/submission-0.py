# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        #BFS is level order traversal so to get maxdept we count the number of levels we have
        #bfs involves a 
        if not root:
            return 0
        level = 0
        q = deque([root])
        while q: #keep going until the que is empty
            for i in range(len(q)): #go through the queue and remove aany element that's currently in it
                root = q.popleft() #remove the element on the left of the q
                if root.left: #check if the left node is present if yesm append it to the q
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            #after looping that level update that one level done by adding one to level   
            level += 1
        return level

