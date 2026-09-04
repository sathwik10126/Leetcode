class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=0
        r=[]
        for i in nums:
            s=s+i
            r.append(s)
        return r

        