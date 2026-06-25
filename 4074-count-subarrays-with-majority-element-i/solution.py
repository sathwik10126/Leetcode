class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)
        c=0
        if target not in nums:
            return 0
        else:
            for i in range(n):
                freq=0
                for j in range(i,n):
                    if nums[j]==target:
                        freq+=1
                    if freq > (j-i+1) //2:
                        c+=1
            return c
