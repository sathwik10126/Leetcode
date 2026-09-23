class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        res=[]
        l=0
        r=n
        while l<n:
            res.append(nums[l])
            l+=1
            res.append(nums[r])
            r+=1
        return res        