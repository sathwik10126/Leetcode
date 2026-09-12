class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res = len(arr)+1
        l=0
        r=0
        s=0
        c=0
        while r<len(arr):
            s=s+arr[r]
            if r-l+1==k:
                if (s)//k>=threshold:
                    c=c+1
                s=s-arr[l]
                l+=1
            r+=1
                       
        return c
        