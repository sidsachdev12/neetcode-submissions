class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, subset):
            # Base case -> Length met
            if index == len(nums):
                res.append(subset.copy()) # copy() since pass by reference
                return

            # Take ther current num or skip it
            subset.append(nums[index])
            backtrack(index+1, subset)
            subset.pop()
            backtrack(index+1, subset)
            return

        backtrack(0, [])
        return res