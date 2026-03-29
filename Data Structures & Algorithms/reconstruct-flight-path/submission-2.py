class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(node):
            if len(res) == len(tickets) + 1:
                return res
            
            if adj[node]==[]:
                return False
            
            temp = adj[node].copy()
            for i, v in enumerate(temp):
                adj[node].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[node].insert(i, v)
                res.pop()
            return False
        dfs("JFK")
        return res
