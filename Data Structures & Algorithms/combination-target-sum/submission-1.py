class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(res, index, state, sum_so_far):

            if sum_so_far == target:
                res.append(state[::])
                return

            if index == len(candidates) or sum_so_far > target:
                return

            state.append(candidates[index])
            sum_so_far += candidates[index]
            
            backtrack(res, index, state, sum_so_far)

            state.pop()
            sum_so_far -= candidates[index]
            backtrack(res, index+1, state, sum_so_far)

            return

        res = []
        backtrack(res, 0, [], 0)
        return res
            