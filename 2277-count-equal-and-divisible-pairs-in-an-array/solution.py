class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        x=len(nums)
        for i in range(x):
            for j in range(i+1,x):
                if nums[i]==nums[j] and ((i*j))%k==0:
                    c=c+1
        return c
        
