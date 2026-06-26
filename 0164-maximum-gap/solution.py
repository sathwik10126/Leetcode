class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=len((nums))
        nums.sort()
        if x<2:
            return 0
        res=[]
        for i in range(1,x):
            res.append((nums[i]-nums[i-1]))
        return max(res) 
        

        
