from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start = 0
        window = s[0 : len(p)]
        window_counter = Counter(window)
        p_counter = Counter(p)
        anagram_indices = []
        if window_counter == p_counter:
            anagram_indices.append(start)

        for i in range(len(s) - len(p)):
            window_counter[s[start]] -= 1
            window_counter[s[i + len(p)]] += 1
            start += 1
            if window_counter == p_counter:
                anagram_indices.append(start)

        return anagram_indices