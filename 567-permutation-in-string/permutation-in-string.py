from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = s2[0: len(s1)]
        window_counter = Counter(window)
        s1_counter = Counter(s1)
        if window_counter == s1_counter:
            return True

        for i in range(len(s2) - len(s1)):
            window_counter[s2[i]] -= 1
            window_counter[s2[i + len(s1)]] += 1
            if window_counter == s1_counter:
                return True

        return False 