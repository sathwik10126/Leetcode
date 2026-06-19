class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=bin(n)[2:].zfill(32)
        k=((r)[::-1])
        j=int(k,2)
        return j

        
