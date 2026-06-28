import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ----------- BRUTE FORCE TECHNIQUE ------------

        # arr = []
        # end = len(nums)


        # while end > 0:

        #     for i in range(end):
        #         curr = 0
        #         for j in range(i, end):
        #             curr += nums[j]

        #         arr.append(curr)
        #     end -= 1

        # return max(arr)

        # ----------- SLIDING WINDOW ---------------
        r = 0
        max_sum = nums[0]
        curr = 0

        while r < len(nums):
            curr += nums[r]
            max_sum = max(max_sum, curr)

            if curr < 0:
                # l = r + 1
                curr = 0

            r += 1

        return max_sum
