class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bs(find_left):
            l=0
            h=len(nums)-1
            boundary=-1
            while l<=h:
                m=(l+h)//2
                if nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    h=m-1
                else:
                    boundary=m
                    if find_left:
                        h=m-1
                    else:
                        l=m+1
            return boundary
        first=bs((True))
        last=bs((False))
        return [first,last]
                        
