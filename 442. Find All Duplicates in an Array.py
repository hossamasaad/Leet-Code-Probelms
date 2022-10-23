class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            
            if nums[abs(num) - 1] < 0:
                res.append(num)
            else:
                nums[abs(num) - 1] = - nums[abs(num) - 1]
        
        return res