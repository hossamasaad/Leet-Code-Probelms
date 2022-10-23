class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        my_set = set()
        n = 0
        for num in nums:
            my_set.add(num)
            if n == len(my_set):
                return num
            n += 1