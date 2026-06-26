class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums_set = set(nums)
        max_cnt = 0
        checked = set()

        for i in range(len(nums)):
            if nums[i] in checked:
                continue
                
            curr = nums[i]
            cnt = 1
            while curr + 1 in nums_set:
                cnt += 1
                curr += 1
                checked.add(curr+1)

            max_cnt =  max(max_cnt, cnt)
        
        return max_cnt


