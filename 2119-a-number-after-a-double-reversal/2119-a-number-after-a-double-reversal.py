class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r1=str(num)[::-1]
        r1=int(r1)
        r2=str(r1)[::-1]
        r2=int(r2)
        if r2==num:
            return True
        else:
            return False
