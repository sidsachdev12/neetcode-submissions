class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        end = max(nums)
        start = min(nums)

        nums_set = set(nums)
        max_cnt = 0

        # for i in range(len(nums)):
        #     curr = nums[i]
        #     cnt = 1
        #     while curr + 1 in nums_set:
        #         cnt += 1
        #         curr += 1

        #     max_cnt =  max(max_cnt, cnt)
        cnt = 1

        while start <= end:
            if start in nums_set and start + 1 in nums_set:
                cnt += 1
            else:
                max_cnt =  max(max_cnt, cnt)
                cnt = 1

            start += 1
        
        return max_cnt


