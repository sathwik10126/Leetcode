class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_j=0
        for i in range(len(nums)):
            if (i>max_j):
                return False
            max_j=max(max_j,i+nums[i])
        return True
        