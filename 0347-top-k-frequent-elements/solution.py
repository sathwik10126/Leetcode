class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        arr=sorted(d.items(),key=lambda x:x[1],reverse=True)
        return[x[0]for x in arr[:k]]

