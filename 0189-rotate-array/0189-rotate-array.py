class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        res=nums[n-k:n]+nums[0:n-k]
        for i in range(n):
            nums[i]=res[i]
        