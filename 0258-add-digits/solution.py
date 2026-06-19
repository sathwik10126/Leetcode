class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            n=0
            for i in str(num):
                n=n+int(i)
            num=n
        return num
            
