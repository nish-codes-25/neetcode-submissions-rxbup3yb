# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None

        self.count = 0
        maximum = root.val

        def dfs(curr, maximum):
            if not curr: return
            
            if curr.val >= maximum:
                maximum = curr.val
                self.count += 1

            left = dfs(curr.left, maximum)
            right = dfs(curr.right, maximum)
            
            return
        dfs(root, maximum)
        return self.count
        
