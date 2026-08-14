class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left <= right:
            c_left = s[left].lower()
            c_right = s[right].lower()

            if not c_left.isalnum():
                left += 1
                continue
            
            if not c_right.isalnum():
                right -= 1
                continue

            if c_left != c_right:
                return False

            left += 1
            right -= 1

        return True
