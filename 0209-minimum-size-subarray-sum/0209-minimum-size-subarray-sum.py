class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        res = len(nums)+1
        l=0
        r=0
        s=0
        while r<len(nums):
            s=s+nums[r]
            while s>=target:
                current_size=r-l+1
                res = min(res,current_size)
                s=s-nums[l]
                l+=1
            r+=1
                       
        if res==len(nums)+1:
            return 0
        else:
            return res
        

        