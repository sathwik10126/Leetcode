class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        for i in nums:
            x=str(i)
            a.append(int(x[::-1]))
        nums=nums+a
        return len(set(nums))
