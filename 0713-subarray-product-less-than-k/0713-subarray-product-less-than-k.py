class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=0
        r=0
        prod=1
        c=0
        if k <= 1:
            return 0
        while r<len(nums):
            prod*=nums[r]
            while prod>=k:
                prod//=nums[l]
                l+=1
            c+=r-l+1
            r+=1
        return c