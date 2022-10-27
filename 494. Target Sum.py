class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def search(i, sums, cache={}):
            if (i, sums) in cache:
                return cache[(i, sums)]

            if i == len(nums):
                if sums == target:
                    cache[(i, sums)] = 1
                else:
                    cache[(i, sums)] = 0

            else:
                cache[(i, sums)] = search(i + 1, sums + nums[i]) + search(i + 1, sums - nums[i])

            return cache[(i, sums)]
            
        return search(0, 0)