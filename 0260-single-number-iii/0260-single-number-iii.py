class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        d=dict()
        for i in nums:
            d[i]=d.get(i,0)+1
        for i in d:
            if d[i] == 1:
                ans.append(i)
        return ans