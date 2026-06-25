class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        vocab = set()
        start, end = 0, 1
        max_cnt = 0

        if len(s) == 0 or len(s) == 1:
            return len(s)

        vocab.add(s[start])
        cnt = 1

        while end < len(s):
            if s[end] in vocab:

                max_cnt = max(max_cnt, cnt)

                while s[start] != s[end]:
                    vocab.remove(s[start])
                    start += 1
                    cnt -= 1

                vocab.remove(s[start])
                start += 1
                cnt -= 1

            cnt += 1
            vocab.add(s[end])
            end += 1
        
        cnt = end - start
        max_cnt = max(max_cnt, cnt)

        return max_cnt
