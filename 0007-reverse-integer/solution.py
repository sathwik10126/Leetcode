class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            rev=-int(str(-x)[::-1])
        else:
            rev=int(str(x)[::-1])
        if -2**31<=rev<=2**31-1:
            return rev
        else:
            return 0
