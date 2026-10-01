class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l=0
        r=0
        d={}
        while(r<len(nums)):
            if nums[r] in d:
                if r-d[nums[r]] <=k:
                    return True
            d[nums[r]]=r
            r+=1
        return False

            
            
        