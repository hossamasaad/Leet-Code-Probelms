class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n    = len(nums)
        self.sums = [0] * (self.n + 1)
        self.sums[0] = nums[0]

        for i in range(1, self.n):
            self.sums[i] = nums[i] + self.sums[i-1]

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.sums[right] - self.sums[left - 1]

        


# Your NumArray object will be instantiated and called as such:

obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
print(param_1)