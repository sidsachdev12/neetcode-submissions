class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        def twoSum(nums, target):
            res = []
            left, right = 0, len(nums) - 1

            while left < right:

                curr_sum = nums[left] + nums[right]

                if curr_sum == target:
                    res.append([nums[left], nums[right]])
                    left += 1

                if curr_sum < target:
                    left += 1
                else:
                    right -= 1

            return res

        nums.sort()
        # visited = set()
        sol = set()

        for i in range(len(nums)):
            val = nums[i]

            copy = nums[::]
            copy.pop(i)

            res = twoSum(copy, -1 * val)
            # print(res)
            if res:
                # print(res)
                for r in res:
                    r.append(val)
                    r.sort()
                    sol.add(tuple(r))

        return list(sol)
        

# -4, -1, -1, 0, 1, 2