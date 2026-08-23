from collections import Counter
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=Counter(nums)
        num=[]
        for i in nums:
            if c[i]>0:
                if num.count(i) < 2:
                    num.append(i)
        nums[:]=num
        return len(nums)

        
