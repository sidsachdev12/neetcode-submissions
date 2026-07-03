class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        final = []
        index = 0
        def dfs(index):
            # base case 1 -> if the index is at its end
            if index >= len(candidates):
                # res = False
                return

            curr.append(candidates[index])
            
            # res = True
            # base case 2 -> if the sum > target
            if sum(curr) > target:
                # res = False
                curr.pop()
                return

           

            # base case 3 -> if the sum == target
            if sum(curr) == target:
                final.append(curr.copy())
                curr.pop()
                return

            # general cases:

            # case 1 -> Take the current one
            res = dfs(index)
            # if not res:
            #     return

            # case 2 -> move onto the next one
            curr.pop()
            dfs(index + 1)
        
        dfs(0)
        return final

            