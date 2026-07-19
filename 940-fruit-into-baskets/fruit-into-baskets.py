from collections import Counter

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        fruit_counter = Counter()
        longest = 0

        for end in range(len(fruits)):
            fruit_counter[fruits[end]] += 1
            while len(fruit_counter) > 2:
                fruit_counter[fruits[start]] -= 1
                if fruit_counter[fruits[start]] == 0:
                    del fruit_counter[fruits[start]]
                start += 1
            longest = max(longest, end - start + 1)
        
        return longest


        