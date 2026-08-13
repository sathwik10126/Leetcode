class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num=dict()
        for i in nums:
            num[i] = num.get(i, 0) + 1
        return max(num, key=num.get)
        
