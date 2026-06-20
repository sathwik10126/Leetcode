class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        l=0
        h=x//2
        ans=1
        while l<=h:
            m=(l+h)//2
            square=m*m
            if square==x:
                return m
            elif square<x:
                ans=m
                l=m+1
            else:
                h=m-1
        return ans
