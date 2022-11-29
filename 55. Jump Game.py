class Solution:
    def canJump(self, nums: list) -> bool:

        pos = 0
        max_pos = 0

        while pos <= max_pos:
            max_pos = max(max_pos, pos+nums[pos])
            pos += 1

            if max_pos >= len(nums) - 1:
                return True
        return False