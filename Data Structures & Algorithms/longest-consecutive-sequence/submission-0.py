class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # max_num = max(nums)
        # min_num = min(nums)
        nums_set = set(nums)
        max_cnt = 0

        for i in range(len(nums)):
            curr = nums[i]
            cnt = 1
            while curr + 1 in nums_set:
                cnt += 1
                curr += 1

            max_cnt =  max(max_cnt, cnt)
        
        return max_cnt


