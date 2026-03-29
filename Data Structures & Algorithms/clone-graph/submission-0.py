"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(curr):
            if not curr:
                return None

            newNode = Node(curr.val)
            newNode.neighbors = []
            visited[newNode.val] = newNode
            for i in curr.neighbors:
                if i.val not in visited:
                    newNode.neighbors.append(dfs(i))
                else:
                    newNode.neighbors.append(visited[i.val])

            return newNode

        x = dfs(node)
        


        return x

