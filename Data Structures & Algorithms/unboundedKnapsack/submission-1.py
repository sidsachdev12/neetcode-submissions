from functools import lru_cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        @lru_cache(None)
        def dfs(index, remaining_capacity):

            if index == len(weight) or remaining_capacity == 0:
                return 0

            # Skip the current
            res = dfs(index + 1, remaining_capacity)

            # Take the current index
            if weight[index] <= remaining_capacity:
                res = max(res, profit[index] + dfs(index, remaining_capacity - weight[index]))
            return res
        
        return dfs(0, capacity)





