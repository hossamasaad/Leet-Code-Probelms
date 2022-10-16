class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        my_set = set()
        for num in nums:
            my_set.add(num)
        
        n = len(nums)
        result = []
        for i in range(1, n+1):
            if i not in my_set:
                result.append(i)
        
        return result