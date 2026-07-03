class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def bt(res, index, state):

            if index == len(nums):
                res.append(state[::])
                return

            state.append(nums[index])
            bt(res, index+1, state)
            
            state.pop()
            bt(res, index+1, state)
            
            return

        res = []
        bt(res, 0, [])
        return res