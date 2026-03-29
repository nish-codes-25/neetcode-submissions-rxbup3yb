# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        res = []
        while queue:
            level = []
            qLen = len(queue)
            for i in range(qLen):
                root = queue.popleft()
                if root:
                    level.append(root.val)
                    queue.append(root.left)
                    queue.append(root.right)
            if level:
                res.append(level)
        return res
