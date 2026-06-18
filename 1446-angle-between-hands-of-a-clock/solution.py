class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        a=abs((30*hour)-(5.5*minutes))
        b=abs(360-a)
        if(a<b):
            return a
        else:
            return b
