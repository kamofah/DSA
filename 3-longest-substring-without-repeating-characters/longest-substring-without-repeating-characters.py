from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        windowCounter = Counter()


        for end in range(len(s)):
            windowCounter[s[end]] += 1
            while windowCounter[s[end]] > 1:
                windowCounter[s[start]] -= 1
                start += 1
            longest = max(longest, end - start + 1)

        return longest