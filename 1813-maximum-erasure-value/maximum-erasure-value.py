from collections import Counter

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        start = 0
        window_sum = 0
        window_counter = Counter()
        max_score = 0

        for end in range(len(nums)):
            window_counter[nums[end]] += 1
            window_sum += nums[end]
            while window_counter[nums[end]] > 1:
                window_sum -= nums[start]
                window_counter[nums[start]] -= 1
                start += 1
            max_score = max(max_score, window_sum)
        
        return max_score
