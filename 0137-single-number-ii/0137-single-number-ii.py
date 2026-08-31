
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        frequency={}
        for i in nums:
            frequency[i] =frequency.get(i,0)+1
        for i in nums:
            if frequency[i]==1:
                return i

        