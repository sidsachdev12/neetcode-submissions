class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:

            vol = min(heights[l], heights[r]) * (r - l)
            max_vol = max(max_vol, vol)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_vol

        