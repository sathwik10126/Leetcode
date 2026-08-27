class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        if not nums:
            return 0
        nums.sort()
        current=1
        longest=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                current=1
            longest=max(longest,current)
        return(longest)
