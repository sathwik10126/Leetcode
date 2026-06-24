class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s=""
        if num==0:
            return str(num)
        x=abs((num))
        while x>0:
            y=x%7
            s=str(y)+s
            x=x//7
        if num<0:
            return "-"+s
        else:
            return s

