class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        def rob_sub(cost):

            cost_so_far = [cost[0], max(cost[0], cost[1])]

            for i in range(2, len(cost)):

                cost_so_far.append(max(cost_so_far[i-1], cost_so_far[i-2] + cost[i]))

            return cost_so_far[-1]
        
        return max(rob_sub(nums[:-1]), rob_sub(nums[1:]))

        
        