class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start = 0
        max_avg = float('-inf')
        window_sum = 0

        for end in range(len(nums)):
            window_sum += nums[end]
            while end - start + 1 > k:
                window_sum -= nums[start]
                start += 1
            if end - start + 1 == k:
                avg = window_sum / (end - start + 1)
                max_avg = max(max_avg, avg)
        
        return max_avg

        