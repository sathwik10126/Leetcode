class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        r=[]
        for _ in range(len(nums)):
            if nums[_]==target:
                r.append(_)
        return r
