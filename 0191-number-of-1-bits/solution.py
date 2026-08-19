class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=list(bin(n)[2:])
        return r.count("1")

