class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        for i in range(len(nums)):
            left = 0 if i == 0 else prefix_sum[i - 1]
            right = 0 if i == len(nums) - 1 else prefix_sum[len(nums) - 1] - prefix_sum[i]

            if left == right:
                return i

        return -1