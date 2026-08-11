class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                r.append(nums[i])
            else:
                break
        x=sum(r)
        while x in nums:
            x=x+1
        return x
