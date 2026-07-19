class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        previous = {}

        for i in range(len(nums)):
            if nums[i] in previous and abs(i - previous[nums[i]]) <= k:
                return True

            previous[nums[i]] = i

        return False        