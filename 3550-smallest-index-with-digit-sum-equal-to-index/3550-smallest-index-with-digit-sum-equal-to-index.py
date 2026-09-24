class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if sum(map(int, str(nums[i]))) == i:
                return i
            i+=1
        return -1