class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        res=[]
        for i in nums:
            if i!=0:
                res.append(i)
        l=[0]*(len(nums)-len(res))
        res=res+l
        for i in range(len(nums)):
            nums[i]=res[i]
            
