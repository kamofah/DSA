class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        initial_prefix_sum = self.nums[0]
        psa = [initial_prefix_sum]
        for i in range(1, len(self.nums)):
            psa.append(psa[i - 1] + self.nums[i])
        if left == 0:
            return psa[right]
        return psa[right] - psa[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)