class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        frequency={}
        for i in nums:
            frequency[i]=frequency.get(i,0)+1
        for j in frequency:
            if frequency[j] > n / 3:
                res.append(j)
        return res
