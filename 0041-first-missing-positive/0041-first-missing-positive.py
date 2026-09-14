class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        m=1
        for i in nums:
            if m==i:
                m=m+1
            elif i > m:
                return m
        return m