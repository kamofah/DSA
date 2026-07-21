class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in previous:
                return [previous[complement], index]
            previous[num] = index
