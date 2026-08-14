class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        i=n
        while True:
            s=1
            for j in str(i):
                s=s*int(j)
            if s%t==0:
                return i
            i=i+1
