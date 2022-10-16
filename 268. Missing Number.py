class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_set = set()
        for num in nums:
            my_set.add(num)
        
        n = len(nums)
        for i in range(n+1):
            if i not in my_set:
                return i
