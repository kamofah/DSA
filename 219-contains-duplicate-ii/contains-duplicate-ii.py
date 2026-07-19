class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        previous = {}

        for index, num in enumerate(nums):
            if nums[index] in previous and index - previous[num] <= k:
                return True

            previous[nums[index]] = index

        return False        