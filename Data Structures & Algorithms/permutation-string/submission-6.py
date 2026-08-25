from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) == 1:
            return s1 in s2

        letters = Counter(s1)

        # sliding window of size len(s1)
        left = 0

        # Check if the characters in window match characters in s1
        for right in range(len(s1), len(s2) + 1):

            window = s2[left:right]
            window_set = Counter(window)

            if letters == window_set:
                return True
            
            left += 1

        # if loop end, return False
        return False