class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n=(nums1+nums2)
        n.sort()
        x=len(n)
        m=x//2
        if(x%2==0):
            return (n[m-1]+n[m])/2.0
        else:
            return n[m]
