class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        r=0
        for i in nums1:
            if i%2!=0:
                r+=1
        if r%2!=0:
            return True
        else:
            return True
