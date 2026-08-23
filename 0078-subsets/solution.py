class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        for i in range(len(nums)):
            for x in res[:]:
                res.append(x + [nums[i]])

        return res

        
