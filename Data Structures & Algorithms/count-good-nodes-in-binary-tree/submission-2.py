# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(curr, maximum):
            if not curr: return 0
            
            res = 1 if curr.val >= maximum else 0
            maximum = max(maximum, curr.val)

            return res + dfs(curr.left, maximum) + dfs(curr.right, maximum)

        return dfs(root, root.val)
        
