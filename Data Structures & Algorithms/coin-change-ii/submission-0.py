class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        coins.sort()

        def dfs(i, a):
            if a == 0:
                return 1
            if i>=len(coins):
                return 0
            if (i, a) in cache:
                return cache[(i, a)]
            
            res = 0
            if coins[i]<=a:
                res = dfs(i, a-coins[i]) + dfs(i+1, a)
                cache[(i,a)] = res
            
            return res
        
        return dfs(0, amount)