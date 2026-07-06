class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # sort the coins - Might not need this
        # coins.sort()
        res = -1

        # dfs to go through each path
        def dfs(index, target, cnt, memo):

            nonlocal res

            if index >= len(coins):
                return

            if res != -1 and cnt > res:
                return

            if target == 0:
                # print(cnt)
                if res == -1:
                    res = cnt
                else:
                    res = min(res, cnt)
                return

            if target < 0:
                return

            # choose the same coin
            same = dfs(index, target - coins[index], cnt + 1, memo)

            # choose next coin
            diff = dfs(index + 1, target, cnt, memo)

            return

        dfs(0, amount, 0, {})
        return res
        