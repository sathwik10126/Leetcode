class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=nums[0]
        for i in range(len(nums)):
            if(nums[i]<mini):
                mini=nums[i]
        return mini
        
