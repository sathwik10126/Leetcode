class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        n= 2**31 - 1
        m= -2**31

        if dividend == m and divisor == -1:
            return n
        if(dividend>0) ^ (divisor>0):
            a=(abs(dividend)//abs(divisor))
            return a*-1
        else:
            return(dividend/divisor)

