class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_set = set(nums)
        longest_seq = 0

        for num in nums:
            # skip if not the first in the sequence
            if num - 1 in my_set:
                continue
            
            length = 1
            while num + 1 in my_set:
                length += 1
                num += 1
            
            longest_seq = max(length, longest_seq)
        return longest_seq