class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x=len(nums)
        for i in range(x):
            s=i
            for j in range(i+1,x):
                if(nums[j]<nums[s]):
                    s=j
                    
            nums[i],nums[s]=nums[s],nums[i]
        return nums
