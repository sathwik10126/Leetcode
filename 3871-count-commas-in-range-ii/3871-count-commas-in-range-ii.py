class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        count=0
        cur=1000
        while cur<=n:
            count+=n-cur+1
            cur*=1000
        return count
        