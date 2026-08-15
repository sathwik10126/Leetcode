class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        c=0
        while n>0:
            n=n//5
            c=c+n
        return c
            


        
