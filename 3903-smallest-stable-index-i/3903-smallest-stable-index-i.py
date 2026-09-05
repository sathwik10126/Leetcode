class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        if n == 1:
            return 0
        i=0
        while i<n:
            left = max(nums[0:i+1])
            right = min(nums[i:n])
            st = left - right
            if st<=k:
                return i
            i+=1
        return -1
        