class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        conver=[]
        res=0
        max_value=0
        for num in nums:
            max_value=max(max_value,num)
            res+=num+max_value
            conver.append(res)

        return conver
        
