class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r=[]
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                r.append(i)
        return r

