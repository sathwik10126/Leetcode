class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r={}
        for i in range(len(nums)):
            b=target-nums[i]
            if b in r:
                return [r[b],i]
            r[nums[i]]=i
            
           

                
        
