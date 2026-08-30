class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=nums.index(min(nums))
        j=nums.index(max(nums))
        left = max(i, j) + 1
        right = len(nums) - min(i, j)
        both = min(i, j) + 1 + len(nums) - max(i, j)
        return (min(left,right,both))