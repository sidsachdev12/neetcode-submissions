class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for c in bin(n)[2:]:
            if c == '1':
                cnt += 1
        return cnt