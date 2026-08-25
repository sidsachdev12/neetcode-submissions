class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 1:
            return s1 in s2

        # letters = set(s1)

        # Sort s1
        # s1_sorted = sorted(s1)

        # sliding window of size len(s1)
        left = 0

        # Check if the characters in window match characters in s1
        for right in range(len(s1), len(s2) + 1):

            window = s2[left:right]
            # window_set = set(window)

            # if not window_set - letters and not letters - window_set:
            if sorted(window) == sorted(s1):
                return True
            
            left += 1

        # if loop end, return False
        return False