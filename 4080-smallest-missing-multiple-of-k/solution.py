class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while True:
            res=k*i
            i+=1
            if res not in nums:
                return res
