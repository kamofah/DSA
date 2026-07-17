from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        window_counter = Counter()


        for end in range(len(s)):
            window_counter[s[end]] += 1
            while window_counter[s[end]] > 1:
                window_counter[s[start]] -= 1
                start += 1
            longest = max(longest, end - start + 1)

        return longest