class Solution(object):
    def minBitwiseArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            found=-1
            for j in range(i):
                if(j|(j+1)==i):
                    found=j
                    break
            a.append(found)
        return a
        
